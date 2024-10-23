import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import config, keyboards, texts

# Include loging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username} ' + texts.start, reply_markup=keyboards.start_kb)

@dp.message_handler(text='О нас')
async def about(message):
    await message.answer(texts.about, reply_markup=keyboards.start_kb)

@dp.message_handler(text='Стоимость')
async def info(message):
    await message.answer('Что Вас интересует?', reply_markup=keyboards.catalog_kb)

# Buy button
@dp.callback_query_handler(text='S')
async def buy_s(call):
    await call.message.answer(texts.price_S, reply_markup=keyboards.buy_kb)
    await call.answer()

@dp.callback_query_handler(text='M')
async def buy_m(call):
    await call.message.answer(texts.price_M, reply_markup=keyboards.buy_kb)
    await call.answer()

@dp.callback_query_handler(text='L')
async def buy_l(call):
    await call.message.answer(texts.price_L, reply_markup=keyboards.buy_kb)
    await call.answer()

@dp.callback_query_handler(text='XL')
async def buy_xl(call):
    await call.message.answer(texts.price_XL, reply_markup=keyboards.buy_kb)
    await call.answer()

@dp.callback_query_handler(text='Other')
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup=keyboards.buy_kb)
    await call.answer()

@dp.callback_query_handler(text='Back')
async def back(call):
    pass

# All another message handler
@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать работать.')




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)