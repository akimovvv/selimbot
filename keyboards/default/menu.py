from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
        [
            KeyboardButton(text="Услуги")
        ],
        [
            KeyboardButton(text="О компании")
        ],
        [
            KeyboardButton(text="Контакты")
        ],
        [
            KeyboardButton(text="Тоже хочу бота )")
        ]
    ])