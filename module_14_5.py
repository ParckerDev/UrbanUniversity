import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

import crud_functions

api = "API"

# Enable logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
crud_functions.initiate_db()



# Keyboard main menu
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = 'Рассчитать'),
            KeyboardButton(text = 'Информация')
        ],
        [
            KeyboardButton(text = 'Купить'),
            KeyboardButton(text = 'Регистрация')
        ]
    ], resize_keyboard = True
    )

# Keyboard inline
kb_prod = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product5', callback_data='product_buying')]
    ]
)

kb_form = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')],
        [InlineKeyboardButton(text='Назад в меню', callback_data='Back')]
    ]
)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

# Start command
@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = menu_kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in crud_functions.get_all_products():
        with open(f'bot1/images/{product[0]}.webp', 'rb') as photo:
            await message.answer_photo(photo, f'Название: {product[1]}\nОписание: {product[2]}\nЦена: {product[3]}руб.')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_prod)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = kb_form)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.callback_query_handler(text='Back')
async def back(call):
    await call.message.answer('Выбери пункт меню:', reply_markup = menu_kb)
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = int(message.text))
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = int(message.text))
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = int(message.text))
    data = await state.get_data()
    await message.answer(f'Ваша норма калорий = {(10 * data["weight"]) + (6.25 * data["growth"]) - (5 * data["age"] + 5)}')
    await state.finish()

@dp.message_handler(text = 'Информация')
async def info(message):
    with open('bot1/images/about.webp', 'rb') as photo:
        await message.answer_photo(photo, 'Привет, я бот для продажи витаминов и расчёта калорий, которые тебе необходимы для снижения веса')



# REGISTRATION BLOCK
@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит)')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not crud_functions.is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer(f'Имя пользователя {message.text} уже есть в базе.\nВведите новое имя пользователя:')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    user = await state.get_data()
    await crud_functions.add_user(user['username'], user['email'], user['age'])
    await state.finish()





# ALL MESSAGE
@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать работать.')


if __name__ =='__main__':
    
    executor.start_polling(dp, skip_updates=True)