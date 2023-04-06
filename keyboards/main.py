from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup


async def get_keyboard():
    """Возвращает клавиатуру о боте"""
    keyboard = InlineKeyboardMarkup()

    first_button = InlineKeyboardButton(f"1) Следующая группа", callback_data="next_group")
    second_button = InlineKeyboardButton(f"2) Следующий человек", callback_data="next_user")
    third_button = InlineKeyboardButton(f"4) Предыдущая группа", callback_data="back_group")
    fourth_button = InlineKeyboardButton(f"3) Предыдущий человек", callback_data="back_user")
    keyboard.add(first_button, second_button)
    keyboard.add(third_button, fourth_button)

    return keyboard
