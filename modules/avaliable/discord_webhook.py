#pylint: disable=missing-docstring
#pylint: disable=import-error

#NOTE: Consider using asynchronous requests lib
from typing import Optional
from fastapi import APIRouter
import requests

# Configuration for discord webhook
WEBHOOK_URL = ""  # Provide the actual Discord webhook URL here

router = APIRouter()


def send_webhook_message(msg: str, username, avatar) -> dict:
    url = WEBHOOK_URL
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "content":msg,
        "username": username, #Optional:Set a custom username for webhook,
        "avatar": avatar # Optional: Set a custom avatar for the webhook
    }
    response = requests.post(url,headers=headers,json=data)
    return {
        "status_code": response.status_code,
        "message": response.text
    }

@router.post("/discord/hook")
def handle_discord_webhook(msg:str,username:Optional[str] = None,avatar:Optional[str] = None) -> dict: #pylint: disable=line-too-long
    response = send_webhook_message(msg,username,avatar)
    if (status_code := response["status_code"]) == 204: #pylint: disable=no-else-return
        return {
            "status": 204,
            "message": "Message sent successfully and no content was returned."
        }
    else:
        return {
            "status": status_code,
            "message": response["message"]
        }
