from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


contact_false = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="WhatsApp", url='https://api.whatsapp.com/send?phone=996500888051'),
            InlineKeyboardButton(text="Telegram", url='https://t.me/@bishkoresar')
        ],
        [
            InlineKeyboardButton(text="Связаться сейчас", callback_data='usual_num_1'),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='back'),
        ]
    ]
)