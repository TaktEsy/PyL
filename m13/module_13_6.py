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

lkb = InlineKeyboardMarkup()
info_but = InlineKeyboardButton(text = "Math calories", callback_data='calories')
form_but = InlineKeyboardButton(text = "Formula of math", callback_data='formula')
lkb.row(info_but, form_but)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Math"), KeyboardButton(text="Info")],
    ], resize_keyboard = True
)
@dp.message_handler(commands=['start'])
async def starter(mess):
    await mess.answer('Choice what you wanna?', reply_markup=start_menu)

@dp.message_handler(text=['Math'])
async def main_menu(mess):
    await mess.answer('Choice one of it', reply_markup=lkb)

@dp.callback_query_handler(text='formula')
async def get_formulas(call):
    await call.message.answer("Mens: 10 х weight (kg) + 6,25 x growth (cm) – 5 х age (y) + 5;")
    await call.message.answer('Womans: 10 x weight (kg) + 6,25 x growth (см) – 5 x age (y) – 161')
    await call.answer()

"""
    1) Make an inheritance!
"""

@dp.callback_query_handler(text = "calories")
async def set_age(call):
    await call.message.answer("How much years is you?")
    await UserState.age.set()
    await call.answer()

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

    await message.answer(f"Norm calories (w): {w}")
    await message.answer(f"Norm calories (m): {m}")
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer(f"@{message.chat.username}'s wrote {message.text}")
    await message.answer(f"Send /start to work!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

