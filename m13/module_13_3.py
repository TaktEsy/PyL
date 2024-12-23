from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f"Добрый день! Что беспокоит?")

@dp.message_handler()
async def all_message(message):
    print(f"@{message.chat.username} напечатал {message.text}")
    await message.answer(f"Ты написал: {message.text}! Напиши старт чтобы начать работу!")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
