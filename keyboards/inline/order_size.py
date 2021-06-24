from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

order_size = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Заказать замер", callback_data='get_size')
        ],
        [
            InlineKeyboardButton(text="Вручную", callback_data='manual_size')
        ]
    ])