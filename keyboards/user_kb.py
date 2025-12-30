from aiogram.utils.keyboard import ReplyKeyboardBuilder

def user_menu_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="📋 Меню")
    kb.button(text="🛎 Вызвать официанта")
    kb.button(text="🛍 Сделать заказ")
    kb.button(text="💳 Оплатить")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
