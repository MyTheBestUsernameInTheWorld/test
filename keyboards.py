from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

main_kb = InlineKeyboardMarkup()
back = InlineKeyboardButton("Главная", callback_data='back')
main_kb.add(back)

menu_kb = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton('Меню 1', callback_data='btn1')
btn2 = InlineKeyboardButton('Меню 2', callback_data='btn2')
btn3 = InlineKeyboardButton('Меню 3', callback_data='btn3')
btn4 = InlineKeyboardButton('Меню 4', callback_data='btn4')
menu_kb.row(btn1, btn2)
menu_kb.row(btn3, btn4)

three_kb = InlineKeyboardMarkup()
th_btn1 = InlineKeyboardButton('Кнопка 1', callback_data='th_btn1')
th_btn2 = InlineKeyboardButton('Кнопка 2', callback_data='th_btn2')
th_btn3 = InlineKeyboardButton('Кнопка 3', callback_data='th_btn3')
three_kb.row(th_btn1, th_btn2, th_btn3)
three_kb.row(back)


def calc(a, b, zn):
    a = int(a)
    b = int(b)
    if zn == '+':
        return a + b
    elif zn == '-':
        return a - b


print(calc(x, z, zn))