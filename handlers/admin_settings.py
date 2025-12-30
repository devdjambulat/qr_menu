from aiogram import Router, types
from config import ADMIN_IDS
from database.db import get_db

router = Router()

@router.message(commands=["settings"])
async def settings_cmd(msg: types.Message):
    if msg.from_user.id not in ADMIN_IDS:
        return

    await msg.answer("Введите новые реквизиты для оплаты:")

@router.message()
async def set_payment(msg: types.Message):
    if msg.from_user.id not in ADMIN_IDS:
        return

    db = get_db()
    db.execute("INSERT INTO settings(payment_info) VALUES (?)", (msg.text,))
    db.commit()

    await msg.answer("Реквизиты обновлены!")
