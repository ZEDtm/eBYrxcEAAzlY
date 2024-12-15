from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import socketio
import json
import asyncio
import time
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List, Dict

from starlette.responses import HTMLResponse

from auth.telegram_auth import auth_telegram_webApp, verify_telegram_data_webApp

from logger import Logger

from config import FAST_API_HOST, FAST_API_PORT, FAST_API_URL ,MONGO_URL, TG_TOKEN_BOT



dummy_users = [
    { "id": 985754362, "name": 'Эдуард', "surname": 'Петров', "phone": '+79234567890' },
    { "id": 735569411, "name": 'Максим', "surname": 'Иванов', "phone": '+76434556678' },
    { "id": 7369362084, "name": 'Дмитрий', "surname": 'Макаров', "phone": '+75236573568' },
    { "id": -1002116285714, "name": 'Алексей', "surname": 'Калашников', "phone": '+73234456245' },
    { "id": -1002332288418, "name": 'Юрий', "surname": 'Белый', "phone": '+71210002553' },
{ "id": 985754362, "name": 'Эдуард', "surname": 'Петров', "phone": '+79234567890' },
    { "id": 735569411, "name": 'Максим', "surname": 'Иванов', "phone": '+76434556678' },
    { "id": 7369362084, "name": 'Дмитрий', "surname": 'Макаров', "phone": '+75236573568' },
    { "id": -1002116285714, "name": 'Алексей', "surname": 'Калашников', "phone": '+73234456245' },
    { "id": -1002332288418, "name": 'Юрий', "surname": 'Белый', "phone": '+71210002553' },
];

# TOKEN = '6819523929:AAHHn_2yAPrP0a7BU8dXouvh7ivDxJUg5O0'
#
# URL = 'localhost:4000'



class Application:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.db = self.client["chat"]
        self.log = Logger()
        self.fast_api = FastAPI()
        self.add_middleware()
        self.message_queue = asyncio.Queue()
        self.sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")
        self.add_socket()
        self.socket_app = socketio.ASGIApp(self.sio)
        self.active_connections = set()
        self.task = None
        self.add_routers()
        self.messages_collection = self.db["messages"]
        self.unread_messages_collection = self.db["unread_messages"]

        self.templates = Jinja2Templates(directory="./build")

    def add_middleware(self):
        self.fast_api.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        @self.fast_api.middleware("http")
        async def check_api_key(request: Request, call_next):
            if request.url.path.startswith("/api"):
                api_key = request.headers.get("Authorization")
                if api_key != "Bearer {}".format(TG_TOKEN_BOT):
                     return JSONResponse(status_code=401, content={"error": "Unauthorized"})
                response = await call_next(request)
                return response
            response = await call_next(request)
            return response

    def add_routers(self):

        @self.fast_api.get("/")
        async def auth_telegram(request: Request):
            init_data = request.query_params.get('initData')
            if not init_data:
                return FileResponse('./build/auth.html')
            user = await verify_telegram_data_webApp(init_data, TG_TOKEN_BOT)
            if user:
                return self.templates.TemplateResponse("index.html", {
                    "request": request,
                    "fast_api_url": FAST_API_URL,
                    "api_key": "{}".format(TG_TOKEN_BOT)
                })
            else:
                return JSONResponse(status_code=401, content={"error": "Unauthorized", "user_id": "".format(user['id'])})

        @self.fast_api.get("/noAuth", response_class=HTMLResponse)
        async def read_root(request: Request):
            return self.templates.TemplateResponse("index.html", {
                "request": request,
                "fast_api_url": FAST_API_URL,
                "api_key": "{}".format(TG_TOKEN_BOT)
            })



        @self.fast_api.get("/api/users")
        async def get_users():
            return JSONResponse(content={"users": dummy_users})

        @self.fast_api.get("/api/messages/{user_id}")
        async def get_messages(user_id: int):
            messages = await self.messages_collection.find({"user": user_id}, {"_id": 0}).to_list(length=None)
            return JSONResponse(content={"messages": [message['message'] for message in messages]})

        @self.fast_api.get("/api/unreadMessages/")
        async def get_unread_messages():
            unread_messages = await self.unread_messages_collection.find({}, {"_id": 0}).to_list(length=None)
            return JSONResponse(content={"unread_messages": unread_messages})

        @self.fast_api.get("/deleteAll")
        async def get_unread_messages():
            await self.messages_collection.delete_many({})
            await self.unread_messages_collection.delete_many({})
            return JSONResponse(content={"status": "OK"})

        @self.fast_api.post("/api/markMessagesAsRead/{user_id}")
        async def mark_messages_as_read(user_id: int):
            # Находим все непрочитанные сообщения для указанного user_id
            unread_messages = await self.unread_messages_collection.find({"user": user_id}).to_list(length=None)

            # Перемещаем сообщения в messages_collection
            if unread_messages:
                await self.messages_collection.insert_many(unread_messages)

            # Удаляем сообщения из unread_messages_collection
            await self.unread_messages_collection.delete_many({"user": user_id})
            self.log.debug(f"Messages have been read for the user {user_id}")
            return JSONResponse(content=[f"Messages have been read for the user {user_id}"])

        @self.fast_api.post("/api/newMessage")
        async def new_message(request: Request):
            new_message = await request.json()
            self.log.debug(new_message)
            if len(self.active_connections) > 0:
                await self.message_queue.put(new_message)
                self.log.debug("Put message to queue")
            else:
                await self.unread_messages_collection.insert_one(new_message)
                self.log.debug("Message was saved")
            return JSONResponse(content=[])

        self.fast_api.mount("/static", StaticFiles(directory="./build/static"), name="static")

    def add_socket(self):
        @self.sio.on('connect')
        async def handle_connect(sid, environ):
            self.log.info(f"Client {sid} connected")
            self.active_connections.add(sid)
            if not self.task:
                self.task = asyncio.create_task(send_update_on_new_message())
                self.log.debug('Task was create')

        async def send_update_on_new_message():
            while True:
                self.log.debug(self.active_connections)
                message = await self.message_queue.get()
                for client in self.active_connections:
                    await self.sio.emit('newMessage', message, room=client)
                    self.log.info(f"Message sent to client {client}")
                await self.unread_messages_collection.insert_one(message)
                self.log.debug("Message was saved")
                self.message_queue.task_done()

        @self.sio.on('disconnect')
        async def handle_disconnect(sid):
            self.active_connections.remove(sid)
            self.log.info(f"Client {sid} disconnected")
            if len(self.active_connections) < 1:
                self.task.done()
                self.task = None
                self.log.debug('Task done')

        @self.sio.on('updateMessage')
        async def handle_update(sid, message):
            if len(self.active_connections) > 1:
                for client in self.active_connections:
                    if client != sid:
                        await self.sio.emit('newMessage', message, room=client)
                        self.log.debug(f'Message for client {client} was update')
                self.log.debug(message)
            await self.messages_collection.insert_one(message)
            self.log.debug("Message was saved")

    def create_app(self):
        return socketio.ASGIApp(self.sio, self.fast_api)


if __name__ == "__main__":
    import uvicorn

    app = Application().create_app()
    uvicorn.run(app, host='0.0.0.0', port=FAST_API_PORT)
