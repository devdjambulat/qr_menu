import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ADMIN_IDS берём из переменной окружения и превращаем в список чисел
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS").split(",")))

DB_PATH = os.getenv("DB_PATH", "database.db")

