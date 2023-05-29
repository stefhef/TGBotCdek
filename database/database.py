"""Основной модуль для работы с БД"""
import logging
import sqlite3
from config import FILENAME


class Database:
    """Класс позволяющий работать с БД"""
    connector = None

    def __init__(self, path="database/") -> None:
        """Подключение к БД"""
        logging.debug("Подключение к БД")
        self.connector = sqlite3.connect(path + FILENAME)

    async def add_user(self, user_id: int, username: str) -> None:
        """Добавление пользователя в БД"""
        logging.info(f"пользователь {user_id} добавлен в БД")
        with self.connector as cursor:
            cursor.execute("""INSERT INTO tg_users(tg_id, username) VALUES($1, $2)""", (user_id, username))

    def test(self):
        """Функция для проверки подключения к БД"""
        with self.connector as cursor:
            print(cursor.execute("SELECT * FROM tg_users").fetchall())

    async def get_info_about_user(self, user_id, forward=1):
        """Получение информации о пользователе из БД"""
        with self.connector as cursor:
            cursor.execute(f"""
                            UPDATE tg_users
                            SET user_id = tg_users.user_id + {forward}
                            WHERE tg_id = $1;""", (user_id,))
            result = cursor.execute("""
                SELECT vk_id, name, surname, phone_number, email, city, status
                FROM users
                WHERE id = (SELECT tg_users.user_id FROM tg_users WHERE tg_id = $1);""", (user_id,)).fetchone()
        return result

    async def get_info_about_group(self, user_id, forward=1):
        """Получение информации о группе из БД"""
        logging.debug(f"Пользователь {user_id} запросил информацию о группе")
        with self.connector as cursor:
            cursor.execute(f"""
                            UPDATE tg_users
                            SET group_id = tg_users.group_id + {forward}
                            WHERE tg_id = $1;""", (user_id,))
            result = cursor.execute("""
                SELECT group_id, name, screen_name, is_closed, type_group, city, country, description, contacts
                FROM groups
                WHERE id = (SELECT tg_users.group_id FROM tg_users WHERE tg_id = $1);""", (user_id,)).fetchone()
        return result


if __name__ == "__main__":
    """Проверка что класс работает и может подключиться к БД"""
    db = Database(path="")
    print(db.get_info_about_user(1))
