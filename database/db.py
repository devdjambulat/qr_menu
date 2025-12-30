import sqlite3
from config import DB_PATH

def get_db():
    """
    Создаёт соединение с базой данных SQLite
    и возвращает объект подключения.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # чтобы можно было обращаться к столбцам по имени
    return conn