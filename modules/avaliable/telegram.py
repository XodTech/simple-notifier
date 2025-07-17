# REQUIRES: aiogram>=3.21.0

#pylint: disable=missing-docstring
#pylint: disable=import-error

from fastapi import APIRouter
from aiogram import Bot

# Configuration for aiogram
BOT_TOKEN = ""  # Telegram bot token (required for authentication)
DESTINATION_ID =0 # Replace it with your actual chat ID, group ID or channel ID

# Message related configuration
DEFAULT_MESSAGE = "Ping"  # Default message to send if no message is provided
MESSAGE_FORMAT = "[msg]" # [msg] will be replaced with an actual message


router = APIRouter()

@router.post("/telegram")
async def handle_telegram(msg:str = DEFAULT_MESSAGE):
    try:
        bot = Bot(token=BOT_TOKEN)
        await bot.send_message(DESTINATION_ID,MESSAGE_FORMAT.replace("[msg]",msg))
        return { "status": 200 }
    except Exception as e :
        return {
            "status": 500,
            "error": f"Internal Server Error: {str(e)}"
        }
