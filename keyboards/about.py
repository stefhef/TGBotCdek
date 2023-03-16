from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from phrases import ABOUT as phrases


async def get_keyboard(user_type: str):
    """Возвращает клавиатуру о боте"""
    keyboard = InlineKeyboardMarkup()

    first_button = InlineKeyboardButton(f"1) {phrases[1]}", callback_data="aboutDeliver")
    second_button = InlineKeyboardButton(f"2) {phrases[2]}", callback_data="manager")
    third_button = InlineKeyboardButton(f"3) {phrases[3]}", callback_data="next_group")
    fourth_button = InlineKeyboardButton(f"4) {phrases[4]}", callback_data="next_user")
    keyboard.add(first_button)
    keyboard.add(second_button)
    keyboard.add(third_button)
    keyboard.add(fourth_button)

    if user_type[0] != "PEOPLE":
        fifth_button = InlineKeyboardButton(f"5) {phrases[5]}", callback_data="conditional")
        keyboard.add(fifth_button)

    return keyboard
