from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup


async def get_keyboard():
    """Возвращает клавиатуру про условия доставки"""
    keyboard = InlineKeyboardMarkup()

    yes_button = InlineKeyboardButton("Да", callback_data="manager")
    no_button = InlineKeyboardButton("Нет", callback_data="main")
    manager_button = InlineKeyboardButton("Связаться с менеджером", callback_data="manager")
    keyboard.row(yes_button, no_button, manager_button)

    return keyboard
