import telebot
from telebot import types

bot = telebot.TeleBot('7857313253:AAGAIT7rTbs5ey66lwt8ASxHOL76zEufaZs')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('🎮 Добавить игру в свой чат', callback_data='add_game')
    btn2 = types.InlineKeyboardButton('🎮 Войти в чат', callback_data='enter_chat')
    btn3 = types.InlineKeyboardButton('🏳️ Язык/Language', callback_data='language')
    btn4 = types.InlineKeyboardButton('👤 Профиль', callback_data='profile')
    btn5 = types.InlineKeyboardButton('🧙‍♀️ Роли', callback_data='roles')
    # Организация кнопок
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(btn4, btn5)

    bot.send_message(message.chat.id, 'Привет!\nЯ бот-ведущий для игры в 👨‍💻Бункер', reply_markup=markup)


bot.polling(non_stop=True)