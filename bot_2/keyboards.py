from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Стоимость'),
        KeyboardButton(text='О нас')
        ]
    ], resize_keyboard = True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Маленькая игра', callback_data='S')],
        [InlineKeyboardButton(text='Стандартная игра', callback_data='M')],
        [InlineKeyboardButton(text='Большая игра', callback_data='L')],
        [InlineKeyboardButton(text='ОЧень большая игра', callback_data='XL')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='Other')]
    ]
)


buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить', url='https://ya.ru')],
        [InlineKeyboardButton('Назад в каталог', callback_data='Back')]
    ]
)

# ADMIN KB
admin_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='users')],
        [InlineKeyboardButton(text='Статистика', callback_data='stat')],
        [
            InlineKeyboardButton(text='Заблокировать', callback_data='block'),
            InlineKeyboardButton(text='Разблокировать', callback_data='unblock')
        ]
    ]
)