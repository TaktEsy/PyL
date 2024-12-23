from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(text=["Ur", "ff", 'DD'])
async def ur_mess(message):
    print(f'Вы написали ключевое слово {message.text}!')

@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Start msg!")

@dp.message_handler()
async def all_message(message):
    print("We get some message!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
