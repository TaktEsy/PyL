from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7442341938:AAH6hyL738xXzGlsNqrO0UFM3z6n8GUBUdc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)