from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



api = 'API'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Keyboard main menu
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = 'Рассчитать'),
            KeyboardButton(text = 'Информация')
        ],
        [
            KeyboardButton(text = 'Купить')
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

# Start command
@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = menu_kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 6):
        with open(f'bot1/images/{i}.webp', 'rb') as photo:
            await message.answer_photo(photo, f'Название: Product{i} | Описание: описание {i} | Цена: {i*100}')
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

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать работать.')


if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True)