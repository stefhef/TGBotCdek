"""Главный модуль для запуска"""
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from database import Database
from keyboards import main_keyboard
from until_function import form_user_info, form_group_info

database = Database()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_command_start(message: types.Message):
    """Обработчик когда пользователь начинает начать"""
    await message.reply('Начало работы', reply_markup=await main_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["next_user"])
async def process_callback_next_user(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = database.get_info_about_user(callback_query.from_user.id)
    if not data:
        await bot.send_message(callback_query.from_user.id, "Нет данных")
        return
    await bot.send_message(callback_query.from_user.id,
                           await form_user_info(data),
                           reply_markup=await main_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["next_group"])
async def process_callback_next_group(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = database.get_info_about_group(callback_query.from_user.id)
    if not data:
        await bot.send_message(callback_query.from_user.id, "Нет данных")
        return
    await bot.send_message(callback_query.from_user.id,
                           await form_group_info(data),
                           reply_markup=await main_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["back_user"])
async def process_callback_back_user(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = database.get_info_about_user(callback_query.from_user.id, forward=-1)
    if not data:
        await bot.send_message(callback_query.from_user.id, "Нет данных")
        return
    await bot.send_message(callback_query.from_user.id,
                           await form_user_info(data),
                           reply_markup=await main_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["back_group"])
async def process_callback_back_group(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = database.get_info_about_group(callback_query.from_user.id, -1)
    if not data:
        await bot.send_message(callback_query.from_user.id, "Нет данных")
        return
    await bot.send_message(callback_query.from_user.id,
                           await form_group_info(data),
                           reply_markup=await main_keyboard())


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
