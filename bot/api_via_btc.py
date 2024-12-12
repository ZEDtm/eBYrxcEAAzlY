import asyncio

import aiohttp
from loguru import logger
from pydantic import BaseModel

from admin_panel.models import TgUser


class DataSchema(BaseModel):
    coin: str
    hashrate_10min: str
    hashrate_1hour: str
    hashrate_24hour: str
    active_workers: int
    unactive_workers: int


class HashRate(BaseModel):
    data: DataSchema

class Balance(BaseModel):
    coin: str
    amount: str

class DataBalance(BaseModel):
    balance: list[Balance]

class BalanceSchema(BaseModel):
    data: DataBalance



async def get_hash_rate(telegram_id: int) -> HashRate:
    user: TgUser = await TgUser.objects.filter(telegram_id=telegram_id).afirst()
    args = {'coin': 'BTC'}
    headers = {'X-API-KEY': user.api_key}

    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.viabtc.net/res/openapi/v1/hashrate', params=args, headers=headers,  ssl=False) as response:
            return HashRate(**await response.json())


async def get_balance(telegram_id: int) -> BalanceSchema:
    user: TgUser = await TgUser.objects.filter(telegram_id=telegram_id).afirst()
    args = {'coin': 'BTC'}
    headers = {'X-API-KEY': user.api_key}


    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.viabtc.net/res/openapi/v1/account', params=args, headers=headers,  ssl=False) as response:
            return BalanceSchema(**await response.json())


