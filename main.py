"""Главный модуль для запуска"""
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from database import Database
from keyboards import main_keyboard
from until_function import form_user_info, form_group_info

database = Database()

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_command_start(message: types.Message):
    """Обработчик когда пользователь начинает начать"""
    await message.reply('Начало работы', reply_markup=await main_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["next_user", "back_user"])
async def process_callback_next_user(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = await database.get_info_about_user(callback_query.from_user.id,
                                              forward=-1 if callback_query.data == "back_user" else 1)
    if not data:
        await bot.send_message(callback_query.from_user.id, "Нет данных")
        return
    await bot.send_message(callback_query.from_user.id,
                           await form_user_info(data),
                           reply_markup=await main_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["next_group", "back_group"])
async def process_callback_next_group(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = await database.get_info_about_group(callback_query.from_user.id,
                                               forward=-1 if callback_query.data == "back_group" else 1)
    if not data:
        await bot.send_message(callback_query.from_user.id, "Нет данных")
        return
    await bot.send_message(callback_query.from_user.id,
                           await form_group_info(data),
                           reply_markup=await main_keyboard())


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
