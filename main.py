import asyncio
import phrases
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from keyboards import welcome_keyboard, about_keyboard, deliver_keyboard
from database import Database

database = Database()
loop = asyncio.get_event_loop().run_until_complete(database.connect())

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_command_1(message: types.Message):
    await message.reply(phrases.FIRST_MESSAGE, reply_markup=await welcome_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["IP", "PEOPLE", "BUSINESS", "main"])
async def process_callback_btn1(callback_query: types.CallbackQuery):
    if callback_query in ["IP", "PEOPLE", "BUSINESS"]:
        await database.add_user(callback_query.from_user.id, callback_query.from_user.username,
                                callback_query.data)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, phrases.ABOUT_TEXT,
                           reply_markup=await about_keyboard(
                               await database.get_user_type(callback_query.from_user.id)))


@dp.callback_query_handler(lambda c: c.data in ["deliver"])
async def process_callback_btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, phrases.DELIVER)


@dp.callback_query_handler(lambda c: c.data in ["aboutDeliver"])
async def process_callback_btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, phrases.ABOUT_DELIVER,
                           reply_markup=await deliver_keyboard())


@dp.callback_query_handler(lambda c: c.data in ["manager"])
async def process_callback_btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, phrases.MANAGER)


@dp.callback_query_handler(lambda c: c.data in ["conditional"])
async def process_callback_btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, phrases.CONDITIONS)


if __name__ == "__main__":
    executor.start_polling(loop=loop, dispatcher=dp, skip_updates=True)
