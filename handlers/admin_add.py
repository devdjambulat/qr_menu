from aiogram import Router, types, F
from config import ADMIN_IDS
from database.db import get_db

router = Router()

add_state = {}

@router.message(commands=["add"])
async def cmd_add(msg: types.Message):
    if msg.from_user.id not in ADMIN_IDS:
        return

    add_state[msg.from_user.id] = {"step": 1}
    await msg.answer("Пришлите фото блюда.")

@router.message(F.photo)
async def add_photo(msg: types.Message):
    uid = msg.from_user.id
    if uid not in add_state or add_state[uid]["step"] != 1:
        return

    add_state[uid]["photo_id"] = msg.photo[-1].file_id
    add_state[uid]["step"] = 2
    await msg.answer("Теперь введите название блюда.")

@router.message()
async def add_steps(msg: types.Message):
    uid = msg.from_user.id
    if uid not in add_state:
        return

    state = add_state[uid]

    if state["step"] == 2:
        state["name"] = msg.text
        state["step"] = 3
        await msg.answer("Введите описание блюда.")
        return

    if state["step"] == 3:
        state["description"] = msg.text
        state["step"] = 4
        await msg.answer("Введите цену блюда.")
        return

    if state["step"] == 4:
        try:
            price = float(msg.text)
        except:
            await msg.answer("Введите число!")
            return

        state["price"] = price

        db = get_db()
        db.execute(
            "INSERT INTO dishes(photo_id, name, description, price) VALUES (?, ?, ?, ?)",
            (state["photo_id"], state["name"], state["description"], state["price"])
        )
        db.commit()

        add_state.pop(uid)

        await msg.answer("Блюдо добавлено в меню!")
