from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import asyncio
import m13.config as config
import crud_functions as crud

bot = Bot(token=config.api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegStage(StatesGroup):
    username = State()
    email = State()
    age = State()

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
        [KeyboardButton(text="Math"), KeyboardButton(text="Info"), KeyboardButton(text="Buy"), KeyboardButton(text="Reg")],
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
    products = crud.select("*", "Products")
    for p in products:
        img = open(f'imgs/b{p[0]}.png', "rb")
        await mess.answer_photo(img, f"Name: {p[1]}\nAbout: {p[2]}\nPrice:  {p[3]} ")

    await mess.answer('Choice product', reply_markup=lkb2)
    crud.connection.close()
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


# Registration
@dp.message_handler(text = ["Reg"])
async def sing_up(msg):
    await msg.answer("Enter the login (only ENG characters):")
    await RegStage.username.set()


@dp.message_handler(state = RegStage.username)
async def set_username(msg, state):
    if crud.is_included(msg.text):
        await msg.answer("Login has been exist!")
        await state.update_data(username=msg.text)
    else:
        await state.update_data(username=msg.text)
        await msg.answer("Enter your email")
        await RegStage.email.set()


@dp.message_handler(state=RegStage.email)
async def set_email(msg, state):
    await state.update_data(email=msg.text)
    await msg.answer("Enter your age")
    await RegStage.age.set()


@dp.message_handler(state=RegStage.age)
async def set_age(msg, state):
    await state.update_data(age=msg.text)
    data = await state.get_data()
    d = data['username'] + data['email'] + data['age']
    crud.add_user(data['username'], data['email'], data['age'])
    await msg.answer(d)


# Other
@dp.message_handler()
async def all_message(message):
    await message.answer(f"@{message.chat.username}'s wrote {message.text}")
    await message.answer(f"Send /start to work!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

