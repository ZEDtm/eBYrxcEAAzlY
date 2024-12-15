import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path)

FAST_API_PORT = os.getenv('FAST_API_PORT')
FAST_API_HOST = os.getenv('FAST_API_HOST')
FAST_API_URL = os.getenv('FAST_API_URL')
MONGO_URL = os.getenv('MONGO_URL')
TG_TOKEN_BOT = os.getenv('TG_TOKEN_BOT')