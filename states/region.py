from aiogram.dispatcher.filters.state import State, StatesGroup

class Service(StatesGroup):
    region_status = State()
    region_true = State()
    region_false = State()
    reg = State()