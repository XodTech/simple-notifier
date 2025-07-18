#pylint: disable=missing-docstring
#pylint: disable=import-error

#NOTE: Consider using asynchronous requests lib
import requests
from fastapi import APIRouter

# Configuration for discord bot
BOT_TOKEN = ""  # Discord bot token (required for authentication)
CHANNEL_ID = "" # Replace with your channel id

router = APIRouter()


def send_message(msg: str) -> dict:
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}",
        "Content-Type": "application/json",
    }
    data = {"content":msg}
    response = requests.post(url,headers=headers,json=data)
    return {
            "status_code": response.status_code,
            "message": response.text #TODO: Format response.text
    }

@router.post("/discord/bot")
def handle_discord_bot(msg:str) -> dict:
    response = send_message(msg)
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
