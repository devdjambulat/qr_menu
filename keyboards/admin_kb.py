from aiogram.utils.keyboard import ReplyKeyboardBuilder

def admin_menu_kb():
    kb = ReplyKeyboardBuilder()
    # здесь можно добавить кнопки для админа
    return kb.as_markup(resize_keyboard=True)
