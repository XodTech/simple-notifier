#pylint: disable=missing-docstring
#pylint: disable=import-error

from fastapi import APIRouter
#from aiogram import Bot
import requests

# Configuration for aiogram
BOT_TOKEN = ""  # Telegram bot token (required for authentication)
DESTINATION_ID = 0 # Replace it with your actual chat ID, group ID or channel ID

# Message related configuration
DEFAULT_MESSAGE = "Ping"  # Default message to send if no message is provided
MESSAGE_FORMAT = "[msg]" # [msg] will be replaced with an actual message


router = APIRouter()

def send_bot_message(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "chat_id": DESTINATION_ID,
        "text": msg
    }

    response = requests.post(url,headers=headers,json=data)
    return {
            "status_code": response.status_code,
            "message": response.text #TODO: Format response.text
    }

@router.post("/telegram")
async def handle_telegram(msg:str = DEFAULT_MESSAGE) -> dict:
    response = send_bot_message(msg)
    if (status_code := response["status_code"]) == 200: #pylint: disable=no-else-return
        return {
            "status": 200,
            "message": "Message sent succesfully"
        }
    else:
        return {
            "status": status_code,
            "message": response["message"]
        }
