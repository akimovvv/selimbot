from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import yes_no, product_categories, product_keyboard, contact_true, contact_false, about_us, order_size, razrabotan
from loader import dp,  bot
import utils.db_api.db_commands as db
from states import Service, Make_order, Menu_contact




@dp.message_handler(text='Тоже хочу бота )')
async def services(message: types.Message):
    text = "Разработан @arturkgz\n" \
           "@bishkek_telegram_bot\n" \
           "Нажмите как Вы хотите связаться"
    await message.answer(text=text, reply_markup=razrabotan)






@dp.message_handler(text='Услуги')
async def services(message: types.Message):
    text = "Выберите интересующий вид конструкции:"
    await message.answer(text=text, reply_markup=product_categories)




@dp.message_handler(text='О компании')
async def services(message: types.Message):
    await Menu_contact.first()
    await message.answer(text='Компания <b>Selim Trade</b> была основана в 2002 году и на протяжении более полутора десятка лет имеет безупречную репутацию.\n\nИндивидуальный подход к решению поставленных задач и рациональная организация рабочего процесса позволяют нам обеспечить самые конкурентоспособные цены на рынке ворот при максимальном качестве производимой продукции и оказываемых услуг.\n\nМы гарантируем вам безупречную работу установленных конструкций и обеспечиваем их простую и экономичную эксплуатацию.\n\nПодобный подход к работе приводит к тому, что все наши клиенты обращаются к нам вновь, рекомендуя нашу компанию своим партнерам, друзьям и знакомым.', reply_markup=about_us)




@dp.message_handler(text='Контакты')
async def services(message: types.Message):
    await Menu_contact.first()
    await message.answer(text='Региональные продажи?', reply_markup=yes_no)




@dp.callback_query_handler(lambda c: c.data == 'contact', state=Menu_contact.menu_contact)
async def take_contact(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer(text='Региональные продажи?', reply_markup=yes_no)




@dp.callback_query_handler(lambda c: c.data == 'address', state=Menu_contact.menu_contact)
async def take_contact(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer(text="<b>Selim Trade</b>\nАйни 22\n1-этаж, 2-офис")
    await call.message.answer_location(latitude=42.848141, longitude=74.587491)
    await state.finish()




@dp.callback_query_handler(lambda c: c.data == 'yes', state=Menu_contact.menu_contact)
async def get_menu_contact(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    text = '<b>Контакты</b>\nНажмите как Вы хотите связаться'
    await call.message.answer(text=text, reply_markup=contact_true)




@dp.callback_query_handler(lambda c: c.data == 'no', state=Menu_contact.menu_contact)
async def get_menu_contact(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    text = '<b>Контакты</b>\nНажмите как Вы хотите связаться'
    await call.message.answer(text=text, reply_markup=contact_false)




@dp.callback_query_handler(lambda c: c.data == 'usual_num_1', state=(Menu_contact.menu_contact, Service.region_false))
async def send_num_1(call: CallbackQuery, state: FSMContext):
    text = "Время работы\nс 9:00 до 18:00"
    await call.answer(cache_time=30, text=text, show_alert=True)
    await call.message.delete()
    await call.message.answer_contact(phone_number='+996500888051', first_name='Selim Trade', last_name='Ворота, рольставни, шлагбаумы')
    await state.finish()




@dp.callback_query_handler(lambda c: c.data == 'usual_num_2', state=(Menu_contact.menu_contact, Service.region_true))
async def send_num_1(call: CallbackQuery, state: FSMContext):
    text = "Время работы\nс 9:00 до 18:00"
    await call.answer(cache_time=30, text=text, show_alert=True)
    await call.message.delete()
    await call.message.answer_contact(phone_number='+996772327676', first_name='Selim Trade', last_name='Ворота, рольставни, шлагбаумы')
    await state.finish()




@dp.callback_query_handler(lambda c: c.data == 'item_1' or c.data == 'item_2' or c.data == 'item_3' or c.data == 'item_4' or c.data == 'item_5' or c.data == 'item_6')
async def service_menu(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await Service.region_status.set()
    if 'item_1' == call.data:
        await call.message.answer_photo(
            photo='AgACAgIAAxkBAAIDlWDRyUeqzR-qQKQKMRz7OsB_o8kcAAKqtDEb2hOQSmEDZPB_znerxqSDny4AAwEAAwIAA3MAA1d1BQABHwQ',
            reply_markup=product_keyboard)
        await state.update_data(item_type='Секционные ворота')
    elif 'item_2' == call.data:
        await call.message.answer_photo(
            photo='AgACAgIAAxkBAAIDl2DRyY38zwn3uUxSpC1mzz6EXhGmAAKrtDEb2hOQSmTcMi3vU3RGojOjoi4AAwEAAwIAA3MAA23oAwABHwQ',
            reply_markup=product_keyboard)
        await state.update_data(item_type='Распашные ворота')
    elif 'item_3' == call.data:
        await call.message.answer_photo(
            photo='AgACAgIAAxkBAAIDn2DRynS0q060_SGM-XXG_cad1BUbAAK2tDEb2hOQSnpJncH_n18r2UHKqS4AAwEAAwIAA3MAA0qsAAIfBA',
            reply_markup=product_keyboard)
        await state.update_data(item_type='Откатные ворота')
    elif 'item_4' == call.data:
        await call.message.answer_photo(
            photo='AgACAgIAAxkBAAIDmWDRyb7th4lOTJpshBAElDkY6PI8AAKxtDEb2hOQStRjBFXJetgngKEAAaQuAAMBAAMCAANzAAPbjgIAAR8E',
            reply_markup=product_keyboard)
        await state.update_data(item_type='Рольставни')
    elif 'item_5' == call.data:
        await call.message.answer_photo(
            photo='AgACAgIAAxkBAAIDm2DRydp-trbbhmk6s3m4J_LZX3dvAAKvtDEb2hOQSu_L_WY1TYuyZNXOqS4AAwEAAwIAA3MAAxKsAAIfBA',
            reply_markup=product_keyboard)
        await state.update_data(item_type='Шлагбаум')
    elif 'item_6' == call.data:
        await call.message.answer_photo(
            photo='AgACAgIAAxkBAAIDnWDRyd71fzGTLHQJ6OL2iZ6MNxUjAAKutDEb2hOQStamtSBfeeVxNqidqC4AAwEAAwIAA3MAA78jAAIfBA',
            reply_markup=product_keyboard)
        await state.update_data(item_type='Технические двери')




@dp.callback_query_handler(lambda c: c.data == 'contacts', state=Service.region_status)
async def get_contacts(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer(text='Региональные продажи?', reply_markup=yes_no)
    await Service.reg.set()
    @dp.callback_query_handler(lambda c: c.data == 'no' or c.data == 'yes', state=Service.reg)
    async def service_menu(call: CallbackQuery):
        await call.answer(cache_time=30)
        if call.data == 'no':
            await call.message.delete()
            text = '<b>Контакты</b>\nНажмите как Вы хотите связаться'
            await call.message.answer(text=text, reply_markup=contact_false)
            await Service.region_false.set()
        else:
            await call.message.delete()
            text = '<b>Контакты</b>\nНажмите как Вы хотите связаться'
            await call.message.answer(text=text, reply_markup=contact_true)
            await Service.region_true.set()




@dp.callback_query_handler(lambda c: c.data == "make_order", state=(Service.region_status))
async def get_order(call: CallbackQuery):
    text = "Вы даёте согласие на обработку введеных Вами данных?"
    await call.answer(cache_time=30, text=text, show_alert=True)
    await call.message.delete()
    await call.message.answer(text='Региональные продажи?', reply_markup=yes_no)

    @dp.callback_query_handler(lambda c: c.data == 'no' or c.data == 'yes', state=Service.region_status)
    async def service_menu(call: CallbackQuery, state: FSMContext):
        await call.answer(cache_time=30)
        await call.message.delete()
        if call.data == 'no':
            await state.update_data(region_status=call.data)
        else:
            await state.update_data(region_status=call.data)
        await call.message.answer(text="Введите свой номер в формате\n0 XXX XXX XXX")
        await Make_order.first()




@dp.message_handler(state=Make_order.get_contact)
async def get_contact(message: types.Message, state: FSMContext):
    await message.delete()
    client_num = message.text.strip().replace(' ', '')
    if client_num.isdigit() and len(client_num) == 10 and client_num[0] == '0':
        await state.update_data(client_num=client_num)
        text = 'Я не знаю, отправьте мастера на бесплатный замер или укажите размер проема'
        await message.answer(text=text, reply_markup=order_size)
        await Make_order.get_size.set()
    else:
        await message.answer(text="Некорректно ввели номер, пожалуйста введите свой номер в формате 0 XXX XXX XXX")
        await Make_order.first()



@dp.callback_query_handler(lambda c: c.data == 'get_size', state=Make_order.get_size)
async def get_size(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(chat_id='-1001393623755',
                           text=f"Региональный: {'Да' if data.get('region_status') == 'yes' else 'Нет'}\nТел. номер: {data.get('client_num')}\nТип ворот: {data.get('item_type')}\nЗаказать бесплатный замер.")
    await call.message.answer(text="Спасибо ваша заявка принята !")
    await call.message.delete()
    await state.finish()



@dp.callback_query_handler(lambda c: c.data == 'manual_size', state=Make_order.get_size)
async def get_size(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    text = "Укажите ширину проёма в м2"
    await call.message.answer(text=text)
    await Make_order.width.set()



@dp.message_handler(state=Make_order.width)
async def get_size(message: types.Message, state: FSMContext):
    if message.text.isdigit() and int(message.text) > 0 and int(message.text) < 1000:
        await state.update_data(width=message.text)
        text = "Укажите высоту проёма в м2"
        await message.answer(text=text)
        await Make_order.lenght.set()
    else:
        text = "Некорректно ввели ширину! Пожалуйста введите ещё раз!"
        await message.answer(text=text)
        await Make_order.width.set()


@dp.message_handler(state=Make_order.lenght)
async def length_size(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and int(text) > 0 and int(text) < 1000:
        data = await state.get_data()
        await bot.send_message(chat_id='-1001393623755',
                               text=f"Региональный: {'Да' if data.get('region_status') == 'yes' else 'Нет'}\nТел. номер: {data.get('client_num')}\nТип ворот: {data.get('item_type')}\nРазмер проёма:\nШирина - {data.get('width')}\nВысота - {text}")
        await message.answer(text="Спасибо ваша заявка принята !")
        await state.finish()
    else:
        text = "Некорректно ввели высоту! Пожалуйста введите ещё раз!"
        await message.answer(text=text)
        await Make_order.lenght.set()





@dp.callback_query_handler(lambda c: c.data == 'back', state=(Service.region_status, Service.region_false, Service.region_true, Menu_contact.menu_contact))
async def go_back(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await state.finish()




@dp.callback_query_handler(lambda c: c.data == 'back')
async def go_back(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await state.finish()