from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

change_lan = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text="Русский", callback_data="lan_ru")],
            [
                InlineKeyboardButton(text="English", callback_data="lan_en"),
                InlineKeyboardButton(text="Deutch", callback_data="lang_de"),
            ]
        ]
    )