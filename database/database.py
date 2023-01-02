"""Основной модуль для работы с БД"""
import asyncio
import asyncpg
from config import HOST, PORT, USER, PASSWORD, DATABASE


class Database:
    """Класс позволяющий работать с БД"""
    connector = None

    async def connect(self) -> None:
        """Подключение к БД"""
        self.connector = await asyncpg.connect(host=HOST, port=PORT, user=USER,
                                               password=PASSWORD, database=DATABASE)

    async def add_user(self, user_id: int, username: str, user_type: str) -> None:
        """Добавление пользователя в БД"""
        await self.connector.execute("""UPDATE users SET user_type=$1""",
                                     user_type) if await self.connector.fetchrow(
            """SELECT * FROM users WHERE user_id=$1""", user_id) else await self.connector.execute(
            """INSERT INTO users(user_id, username, user_type) VALUES($1, $2, $3)""", user_id,
            username, user_type)

    async def get_user_type(self, user_id) -> str:
        """Функция для получения 'типа пользователя'"""
        record = await self.connector.fetchrow("""SELECT user_type FROM users
        WHERE user_id=$1""", user_id)
        return record.get("user_type")


if __name__ == "__main__":
    db = Database()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.connect())
    res = loop.run_until_complete(db.get_user_type(662150107))
    print(res.get("user_type"))
