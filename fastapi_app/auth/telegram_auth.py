import hashlib
from fastapi import Request
from urllib.parse import unquote
import hmac
import json
import time

async def auth_telegram_webApp(request: Request, token):
    data = await request.json()
    if not data['initData']:
        return False
    init_data = data['initData']
    user = verify_telegram_data_webApp(init_data, token)
    if user:
        return user
    return False

async def verify_telegram_data_webApp(init_data, bot_token):
    """
    Verifies data from Telegram.WebApp.InitData
    """
    vals = {k: unquote(v) for k, v in [s.split('=', 1) for s in init_data.split('&')]}
    data_check_string = '\n'.join(f"{k}={v}" for k, v in sorted(vals.items()) if k != 'hash')
    secret_key = hmac.new("WebAppData".encode(), bot_token.encode(), hashlib.sha256).digest()
    h = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256)
    if not h.hexdigest() == vals['hash']:
        return False
    auth_date = int(vals['auth_date'])
    if time.time() - auth_date > 86400:  # 24 hours
        return False
    user_data = json.loads(vals['user'])
    return user_data