from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup


async def get_keyboard():
    """Возвращает клавиатуру для определения типа пользователя"""
    keyboard = InlineKeyboardMarkup()

    fiz_button = InlineKeyboardButton("Физ лицо", callback_data="PEOPLE")
    bus_button = InlineKeyboardButton("Юр лицо", callback_data="BUSINESS")
    ip_button = InlineKeyboardButton("ИП", callback_data="IP")
    keyboard.row(fiz_button, bus_button, ip_button)
    return keyboard
