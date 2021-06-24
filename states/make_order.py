from aiogram.dispatcher.filters.state import State, StatesGroup

class Make_order(StatesGroup):
    get_contact = State()
    get_size = State()
    lenght = State()
    width = State()