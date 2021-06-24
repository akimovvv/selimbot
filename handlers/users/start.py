from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default import main_menu_keyboard
from loader import dp
import utils.db_api.db_commands as db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await db.add_user(id=message.from_user.id, username=message.from_user.username)
    text = "Добрый день {user} ! Вас приветствует Selim Bot !".format(user=message.from_user.full_name)
    await message.answer(text=text, reply_markup=main_menu_keyboard)