from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


api = "api"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard = True)
button_calculate = KeyboardButton(text = 'Рассчитать')
button_info = KeyboardButton(text = 'Информация')
kb.add(button_calculate)
kb.add(button_info)

kb_inline = InlineKeyboardMarkup()
button_get_calc = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formula = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.add(button_get_calc)
kb_inline.add(button_formula)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = kb_inline)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

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
    await message.answer('Привет, я бот для расчёта калорий, которые тебе необходимы для поддержания своего веса')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать работать.')


if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True)