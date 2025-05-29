import asyncio
from aiogram import Bot, Dispatcher

from config import TELEGRAM_BOT_TOKEN
from handlers import router


async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
