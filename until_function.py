async def form_user_info(data: list | tuple):
    return f'<b>Информация о пользователе ВК</b>:\n' \
           f'<b>ID пользователя</b>: {data[0]}\n' \
           f'<b>Фамилия имя</b>: {data[1]} {data[2]}\n' \
           f'<b>Телефонный номер</b>:\t{data[3] if not (data[3] is None or data[3] == "None") else "Телефонный номер не указан"}\n' \
           f'<b>Почта</b>: {data[4] if data[4] else "Почта не указана"}\n' \
           f'<b>Город</b>: {data[5] if data[5] else "Город не указан"}\n' \
           f'<b>Статус</b>: {data[6]}'


async def form_group_info(data: list | tuple):
    contacts = "\n"
    if data != "None":
        for number, item, in enumerate(data[8].replace("[", "").split("]")[:-2], 1):
            contacts += f"<b>Контакт номер {number}:</b>\n"
            item = item.split(", ")
            contacts += f"<b>ID</b>: {item[0] if item[0] != 'None' else 'Не указан'}\n" \
                        f"<b>Должность</b>: {item[1] if item[1] != 'None' else 'Не указана'}\n" \
                        f"<b>Номер телефона</b>: {item[2] if item[2] != 'None' else 'Не указан'}\n" \
                        f"<b>Почта</b>: {item[3] if item[3] != 'None' else 'Не указана'}\n\n"
    return f'<b>ID группы</b>: {data[0]}\n' \
           f'<b>Название</b>: {data[1]}\n' \
           f'<b>ScreenName</b>: {data[2]}\n' \
           f'<b>Закрыта ли</b>: {"Да" if data[3] else "Нет"}\n' \
           f'<b>Тип группы</b>: {data[4]}\n' \
           f'<b>Город</b>: {data[5] if data[5] != "None" else "Не указан"}\n' \
           f'<b>Страна</b>: {data[6] if data[6] != "None" else "Не указана"}\n' \
           f'<b>Описание группы</b>:\n\n{data[7] if data[7] else "Отсутствует"}\n' \
           f'{contacts if data[8] != "None" else "<b>Контакты отсутствуют</b>"}'
