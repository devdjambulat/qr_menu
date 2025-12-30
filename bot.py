import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.models import create_tables

# Подключаем все обработчики
from handlers.start import router as start_router
from handlers.user_menu import router as menu_router
from handlers.admin_add import router as add_router
from handlers.admin_edit import router as edit_router
from handlers.admin_settings import router as settings_router
from handlers.admin_group import router as group_router


async def main():
    # создаём объект бота
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    # создаём таблицы в базе данных
    create_tables()

    # подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(add_router)
    dp.include_router(edit_router)
    dp.include_router(settings_router)
    dp.include_router(group_router)

    # запускаем бота
    await dp.start_polling(bot)


if name == "main":
    asyncio.run(main())