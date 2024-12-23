from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = "Calories")
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

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
