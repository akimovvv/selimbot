from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

product_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Контакты", callback_data='contacts'),
            InlineKeyboardButton(text="Сделать заказ", callback_data='make_order')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='back'),
        ]
    ]
)