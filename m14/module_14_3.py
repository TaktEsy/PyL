from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import asyncio
import m13.config as config

bot = Bot(token=config.api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

lkb = InlineKeyboardMarkup()
info_but = InlineKeyboardButton(text = "Math calories", callback_data='calories')
form_but = InlineKeyboardButton(text = "Formula of math", callback_data='formula')
lkb.row(info_but, form_but)

lkb2 = InlineKeyboardMarkup()
item1 = InlineKeyboardButton(text = "Product1", callback_data='product_buying')
item2 = InlineKeyboardButton(text = "Product2", callback_data='product_buying')
item3 = InlineKeyboardButton(text = "Product3", callback_data='product_buying')
item4 = InlineKeyboardButton(text = "Product4", callback_data='product_buying')
lkb2.row(item1, item2, item3, item4)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Math"), KeyboardButton(text="Info"), KeyboardButton(text="Buy")],
    ], resize_keyboard = True
)
@dp.message_handler(commands=['start'])
async def starter(mess):
    await mess.answer('Hello, I HP-upper bot', reply_markup=start_menu)

@dp.message_handler(text=['Math'])
async def main_menu(mess):
    await mess.answer('Choice one of it', reply_markup=lkb)

@dp.message_handler(text=['Buy'])
async def get_buying_list(mess):

    with open('imgs/b1.png', "rb") as b1, open('imgs/b2.png', "rb") as b2, open('imgs/b3.png', "rb") as b3, open('imgs/b4.png', "rb") as b4:
        await mess.answer_photo(b1, "Name: B1 Vitamin | About: BUY IT NOW! | Price: 101$")
        await mess.answer_photo(b2, "Name: B2 Vitamin | About: BUY IT NOW TOO! | Price: 202$")
        await mess.answer_photo(b3, "Name: B3 Vitamin | About: BUY IT NOW TOO! | Price: 303$")
        await mess.answer_photo(b4, "Name: B4 Vitamin | About: BUY IT NOW TOO! | Price: 404$")
        await mess.answer('Choice product', reply_markup=lkb2)

@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer("Good buying, see you later!")
    await call.answer()


@dp.callback_query_handler(text='formula')
async def get_formulas(call):
    await call.message.answer("Mens: 10 х weight (kg) + 6,25 x growth (cm) – 5 х age (y) + 5;")
    await call.message.answer('Womans: 10 x weight (kg) + 6,25 x growth (см) – 5 x age (y) – 161')
    await call.answer()

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

