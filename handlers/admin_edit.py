from aiogram import Router, types
from config import ADMIN_IDS
from database.db import get_db

router = Router()

edit_state = {}

@router.message(commands=["edit"])
async def cmd_edit(msg: types.Message):
    if msg.from_user.id not in ADMIN_IDS:
        return

    db = get_db()
    dishes = db.execute("SELECT id, name FROM dishes").fetchall()

    if not dishes:
        await msg.answer("Меню пустое.")
        return

    text = "Выберите ID блюда для редактирования:\n\n"
    for d in dishes:
        text += f"{d['id']}. {d['name']}\n"

    edit_state[msg.from_user.id] = {"step": 1}

    await msg.answer(text)

@router.message()
async def edit_flow(msg: types.Message):
    uid = msg.from_user.id
    if uid not in edit_state:
        return

    st = edit_state[uid]
    db = get_db()

    if st["step"] == 1:
        try:
            dish_id = int(msg.text)
        except:
            await msg.answer("Введите ID числом.")
            return

        st["dish_id"] = dish_id
        st["step"] = 2

        await msg.answer("Что изменить?\n1 — Название\n2 — Описание\n3 — Цена\n4 — Фото")
        return

    if st["step"] == 2:
        choice = msg.text

        if choice == "1":
            st["field"] = "name"
            st["step"] = 3
            await msg.answer("Введите новое название:")
        elif choice == "2":
            st["field"] = "description"
            st["step"] = 3
            await msg.answer("Введите новое описание:")
        elif choice == "3":
            st["field"] = "price"
            st["step"] = 3
            await msg.answer("Введите новую цену:")
        elif choice == "4":
            st["field"] = "photo"
            st["step"] = 4
            await msg.answer("Отправьте новое фото.")
        else:
            await msg.answer("Введите число от 1 до 4.")
        return

    if st["step"] == 3:
        value = msg.text
        if st["field"] == "price":
            try:
                value = float(value)
            except:
                await msg.answer("Цена должна быть числом.")
                return

        db.execute(
            f"UPDATE dishes SET {st['field']} = ? WHERE id = ?",
            (value, st["dish_id"])
        )
        db.commit()
        edit_state.pop(uid)
        await msg.answer("Блюдо обновлено!")

    if st["step"] == 4:
        if not msg.photo:
            await msg.answer("Пришлите фото.")
            return

        file_id = msg.photo[-1].file_id
        db.execute(
            "UPDATE dishes SET photo_id=? WHERE id=?",
            (file_id, st["dish_id"])
        )
        db.commit()
        edit_state.pop(uid)
        await msg.answer("Фото обновлено!")
