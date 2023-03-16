"""Основной модуль для работы с БД"""
import sqlite3
from config import FILENAME


class Database:
    """Класс позволяющий работать с БД"""
    connector = None

    def __init__(self, path="database/") -> None:
        """Подключение к БД"""
        self.connector = sqlite3.connect(path + FILENAME)

    def test(self):
        with self.connector as cursor:
            print(cursor.execute("SELECT * FROM tg_users").fetchall())

    def add_user(self, user_id: int, username: str, user_type: str) -> None:
        """Добавление пользователя в БД"""
        with self.connector as cursor:
            cursor.execute("""UPDATE tg_users SET user_type=$1""", [user_type]) if cursor.execute(
                """SELECT * FROM tg_users WHERE tg_id=$1""", [user_id]).fetchone() else cursor.execute(
                """INSERT INTO tg_users(tg_id, username, user_type) VALUES($1, $2, $3)""", (user_id,
                                                                                            username, user_type))

    def get_user_type(self, user_id) -> str:
        """Функция для получения 'типа пользователя'"""
        with self.connector as cursor:
            record = cursor.execute("""SELECT user_type FROM tg_users WHERE tg_id=$1""", (user_id,)).fetchone()
        return record

    def get_info_about_user(self, user_id):
        with self.connector as cursor:
            result = cursor.execute("""
                SELECT vk_id, name, surname, phone_number, email, city
                FROM users
                WHERE id = (SELECT tg_users.user_id FROM tg_users WHERE tg_id = $1);""", (user_id,)).fetchone()
            cursor.execute("""
                UPDATE tg_users
                SET user_id = tg_users.user_id + 1
                WHERE tg_id = $1;""", (user_id,))
        return result

    def get_info_about_group(self, user_id):
        with self.connector as cursor:
            result = cursor.execute("""
                SELECT group_id, name, screen_name, is_closed, type_group, city, country, description, contacts
                FROM groups
                WHERE id = (SELECT tg_users.group_id FROM tg_users WHERE tg_id = $1);""", (user_id,)).fetchone()
            cursor.execute("""
                UPDATE tg_users
                SET group_id = tg_users.group_id + 1
                WHERE tg_id = $1;""", (user_id,))
        return result


if __name__ == "__main__":
    db = Database(path="")
    print(db.get_info_about_user(1))
