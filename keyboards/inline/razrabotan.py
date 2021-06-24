from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

razrabotan = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram", url='https://t.me/arturkgz'),
            InlineKeyboardButton(text="WhatsApp", url='https://api.whatsapp.com/send?phone=996500060402'),
        ],
        [
            InlineKeyboardButton(text="Наш бот", url='https://t.me/bishkek_telegram_bot')
        ]
    ])