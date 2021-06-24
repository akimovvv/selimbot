from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

contact_true = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="WhatsApp", url='https://api.whatsapp.com/send?phone=996772327676'),
        ],
        [
            InlineKeyboardButton(text="Связаться сейчас", callback_data='usual_num_2'),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='back'),
        ]
    ]
)