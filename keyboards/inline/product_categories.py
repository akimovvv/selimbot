from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

product_categories = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Секционные ворота", callback_data='item_1'),
            InlineKeyboardButton(text="Распашные ворота", callback_data='item_2')
        ],
        [
            InlineKeyboardButton(text="Откатные ворота", callback_data='item_3'),
            InlineKeyboardButton(text="Рольставни", callback_data='item_4')
        ],
        [
            InlineKeyboardButton(text="Шлагбаум", callback_data='item_5'),
            InlineKeyboardButton(text="Технические двери", callback_data='item_6')
        ],
        [
            InlineKeyboardButton(text="Назад в Instagram",  url='https://instagram.com/selimtrade?utm_medium=copy_link')
        ]
    ]
)