import logging
import asyncio
import os

from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
from hendlers import router

load_dotenv()

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=os.environ['TOKEN'])
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:

        print('Выход...........')
