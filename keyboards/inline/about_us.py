from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

about_us = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Контакты", callback_data='contact'),
            InlineKeyboardButton(text="Адреса", callback_data='address')
        ],
        [
            InlineKeyboardButton(text="Instagram", url='https://www.instagram.com/selimtrade/?utm_medium=copy_link'),
        ]
    ])