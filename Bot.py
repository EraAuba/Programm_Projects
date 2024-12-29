import telebot
import webbrowser

bot = telebot.TeleBot('7857313253:AAGAIT7rTbs5ey66lwt8ASxHOL76zEufaZs')

@bot.message_handler(commands=['start']) 
def main(message):
    bot.send_message(message.chat.id , f'Привет, {message.from_user.first_name}')
    
@bot.message_handler() 
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')



bot.polling(non_stop=True)