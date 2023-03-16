"""Главный модуль для запуска"""
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from keyboards import welcome_keyboard, about_keyboard, deliver_keyboard
from database import Database
import phrases

database = Database()
# loop = asyncio.get_event_loop()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_command_start(message: types.Message):
    """Обработчик когда пользователь начинает начать"""
    await message.reply(phrases.FIRST_MESSAGE, reply_markup=await welcome_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["IP", "PEOPLE", "BUSINESS", "main"])
async def process_callback_type_user(callback_query: types.CallbackQuery):
    """Обработчик, который отсылает возможности бота"""
    if callback_query.data in ["IP", "PEOPLE", "BUSINESS"]:
        database.add_user(callback_query.from_user.id, callback_query.from_user.username,
                          callback_query.data)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, phrases.ABOUT_TEXT,
                           reply_markup=await about_keyboard(
                               database.get_user_type(callback_query.from_user.id)))


@dp.callback_query_handler(lambda c: c.data in ["aboutDeliver"])
async def process_callback_about_deliver(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, phrases.ABOUT_DELIVER,
                           reply_markup=await deliver_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["manager"])
async def process_callback_manager(callback_query: types.CallbackQuery):
    """"""
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Ожидайте")


@dp.callback_query_handler(lambda c: c.data in ["conditional"])
async def process_callback_conditional(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, phrases.CONDITIONS)


@dp.callback_query_handler(lambda c: c.data in ["next_user"])
async def process_callback_next_user(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = database.get_info_about_user(callback_query.from_user.id)
    if not data:
        await bot.send_message(callback_query.from_user.id, "Нет данных")
        return
    await bot.send_message(callback_query.from_user.id,
                           f'Информация о пользователе ВК:\n'
                           f'ID пользователя: {data[0]}\nФамилия имя: {data[1]}'
                           f'\nТелефонный номер:\t{data[2] if data[2] else "Телефонный номер не указан"}'
                           f'\nПочта: {data[3] if data[3] else "Почта не указана"}'
                           f'\nГород: {data[4] if data[4] else "Город не указан"}'
                           f'\nСтатус: {data[5]}')


@dp.callback_query_handler(lambda c: c.data in ["next_group"])
async def process_callback_next_group(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = database.get_info_about_group(callback_query.from_user.id)
    if not data:
        await bot.send_message(callback_query.from_user.id, "Нет данных")
        return
    await bot.send_message(callback_query.from_user.id,
                           f'ID группы: {data[0]}\nНазвание: {data[1]}\nScreenName: {data[2]}\nЗакрыта ли: {"Да" if data[3] else "Нет"}\nТип группы: {data[4]}\nГород: {data[5] if data[5] else "Город не указан"}\nСтрана: {data[6] if data[6] else "Старна не указана"}\nОписание группы: {data[6] if data[6] else "Без описания"}\nКонтакты: {data[7] if data[7] else "Нет контактов"}')


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
