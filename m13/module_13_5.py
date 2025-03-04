from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import asyncio
import config

api = config.api
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup()
math_but = KeyboardButton(text = "Math")
info_but = KeyboardButton(text = "Info")
kb.row(math_but,info_but)


@dp.message_handler(commands=['start'])
async def start(mess):
    await mess.answer('Hi!', reply_markup = kb)

"""
    1) Это надо наследовать с предыдущего модуля!!!!
    2) При импорте предыдущего модуля ругается на api ключ (отсутствие)
"""
@dp.message_handler(text = "Math")
async def set_age(message):
    await message.answer("How much years is you?")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("How is growth?")
    await state.update_data(growth=message.text)
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("How is weight?")
    await state.update_data(growth=message.text)
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    m = 10*int(data['weight']) + 6.25*int(data['growth']) - 5*int(data['age']) + 5
    w = 10*int(data['weight']) + 6.25*int(data['growth']) - 5*int(data['age']) - 161

    await message.answer(f"Норма каллорий (жен): {w}")
    await message.answer(f"Норма каллорий (муж): {m}")
    await state.finish()

@dp.message_handler()
async def all_message(message):
    print(f"@{message.chat.username} напечатал {message.text}")
    await message.answer(f"Ты написал: {message.text}! Напиши /start чтобы начать работу!")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
