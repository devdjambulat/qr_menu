from database.db import get_db

def create_tables():
    """
    Создаёт все таблицы в базе данных, если их ещё нет:
    - dishes: блюда меню
    - waiter_groups: группы официантов
    - settings: настройки оплаты
    """
    db = get_db()
    cur = db.cursor()

    # Таблица с блюдами
    cur.execute("""
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            photo_id TEXT,
            name TEXT,
            description TEXT,
            price REAL
        )
    """)

    # Таблица с группами официантов
    cur.execute("""
        CREATE TABLE IF NOT EXISTS waiter_groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER
        )
    """)

    # Таблица с настройками (например, реквизиты оплаты)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payment_info TEXT
        )
    """)

    db.commit()
    db.close()