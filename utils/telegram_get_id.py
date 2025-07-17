#pylint: disable=missing-docstring
#pylint: disable=import-error

# /// script
# requires-python = ">=3.13"
# dependencies = [
#    "aiogram>=3.21.0"
# ]
# ///

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = ""  # Telegram bot token (required for authentication)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_get_id(message: Message) -> None:
    await message.reply(f"Your chat id: {message.chat.id}")

async def main() -> None :
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot up and running!")
    asyncio.run(main())
