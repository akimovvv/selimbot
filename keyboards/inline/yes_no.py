from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yes_no = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data='yes'),
            InlineKeyboardButton(text="Нет", callback_data='no')
        ]
    ])