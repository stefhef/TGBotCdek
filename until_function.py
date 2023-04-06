async def form_user_info(data):
    return f'Информация о пользователе ВК:\n' \
           f'ID пользователя: {data[0]}\n' \
           f'Фамилия имя: {data[1]} {data[2]}\n' \
           f'Телефонный номер:\t{data[3] if not (data[3] is None or data[3] == "None") else "Телефонный номер не указан"}\n' \
           f'Почта: {data[4] if data[4] else "Почта не указана"}\n' \
           f'Город: {data[5] if data[5] else "Город не указан"}\n' \
           f'Статус: {data[6]}'


async def form_group_info(data):
    return f'ID группы: {data[0]}\n' \
           f'Название: {data[1]}\n' \
           f'ScreenName: {data[2]}\n' \
           f'Закрыта ли: {"Да" if data[3] else "Нет"}\n' \
           f'Тип группы: {data[4]}\n' \
           f'Город: {data[5] if data[5] != "None" else "Город не указан"}\n' \
           f'Страна: {data[6] if data[6] != "None" else "Старна не указана"}\n' \
           f'Описание группы: {data[7] if data[7] else "Без описания"}\n' \
           f'Контакты: {data[8] if data[8] else "Нет контактов"}'
