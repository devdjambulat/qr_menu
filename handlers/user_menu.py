from aiogram import Router, types
from database.db import get_db

router = Router()


@router.message(lambda m: m.text == "📋 Меню")
async def show_menu(msg: types.Message):
    db = get_db()
    dishes = db.execute("SELECT * FROM dishes").fetchall()

    if not dishes:
        await msg.answer("Меню пока пусто.")
        return

    for d in dishes:
        await msg.answer_photo(
            photo=d["photo_id"],
            caption=f"🍽 {d['name']}\n\n{d['description']}\n\nЦена: {d['price']} руб."
        )


@router.message(lambda m: m.text == "🛎 Вызвать официанта")
async def call_waiter(msg: types.Message):
    db = get_db()
    groups = db.execute("SELECT chat_id FROM waiter_groups").fetchall()

    if not groups:
        await msg.answer("Нет подключённых групп официантов.")
        return

    for g in groups:
        await msg.bot.send_message(g["chat_id"], f"🛎 Столик прислал запрос на обслуживание.")

    await msg.answer("Официант скоро подойдёт!")


@router.message(lambda m: m.text == "💳 Оплатить")
async def pay(msg: types.Message):
    db = get_db()
    row = db.execute("SELECT payment_info FROM settings ORDER BY id DESC LIMIT 1").fetchone()

    if not row or not row["payment_info"]:
        await msg.answer("Способ оплаты ещё не настроен.")
    else:
        await msg.answer(f"💳 Реквизиты для оплаты:\n\n{row['payment_info']}")
