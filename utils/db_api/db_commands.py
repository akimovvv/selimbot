from asyncpg import UniqueViolationError

from utils.db_api.schemas import User

#  creat in db user schemas
async def add_user(id: int,
                   username: str,
                   language: str = None,
                   name: str = None,
                   gender: int = None,
                   age: int = None,
                   number: int = None,
                   agreement: int = None):
    try:
        user = User(id=id, username=username, language=language, name=name, gender=gender, age=age, number=number, agreement=agreement)
        await user.create()
    except UniqueViolationError:
        pass

# for selct user by id
async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user



# for update user data`s
async def update_user_language(id, language):
    user = await User.get(id)
    await user.update(language=language).apply()

async def update_user_name(id, name):
    user = await User.get(id)
    await user.update(name=name).apply()

async def update_user_gender(id, gender):
    user = await User.get(id)
    await user.update(gender=gender).apply()

async def update_user_age(id, age):
    user = await User.get(id)
    await user.update(age=age).apply()

async def update_user_number(id, number):
    user = await User.get(id)
    await user.update(number=number).apply()

async def update_user_agreement(id, agreement):
    user = await User.get(id)
    await user.update(number=agreement).apply()




# Profile
# ____________________________________________________________________________________
async def add_user(id: int,
                   username: str,
                   language: str = None,
                   name: str = None,
                   gender: int = None,
                   age: int = None,
                   number: int = None):
    try:
        user = User(id=id, username=username, language=language, name=name, gender=gender, age=age, number=number)
        await user.create()
    except UniqueViolationError:
        pass

async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user




async def update_user_language(id, language):
    user = await User.get(id)
    await user.update(language=language).apply()

async def update_profile_name(id, name):
    user = await User.get(id)
    await user.update(name=name).apply()

async def update_profile_gender(id, gender):
    user = await User.get(id)
    await user.update(gender=gender).apply()

async def update_profile_age(id, age):
    user = await User.get(id)
    await user.update(age=age).apply()

async def update_profile_number(id, number):
    user = await User.get(id)
    await user.update(number=number).apply()