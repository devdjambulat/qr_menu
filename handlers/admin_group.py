from aiogram import Router, types
from config import ADMIN_IDS
from database.db import get_db

router = Router()

@router.message(commands=["group"])
async def add_group(msg: types.Message):
    if msg.from_user.id not in ADMIN_IDS:
        return

    chat_id = msg.chat.id

    db = get_db()
    db.execute("INSERT INTO waiter_groups(chat_id) VALUES (?)", (chat_id,))
    db.commit()

    await msg.answer("Группа официантов успешно добавлена!")
