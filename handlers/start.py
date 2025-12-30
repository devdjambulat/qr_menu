from aiogram import Router, types
from keyboards.user_kb import user_menu_kb

router = Router()

@router.message(commands=["start"])
async def start_cmd(msg: types.Message):
    await msg.answer(
        "Добро пожаловать в QR-меню!\nВыберите действие:",
        reply_markup=user_menu_kb()
    )
