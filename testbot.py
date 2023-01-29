import telebot

bot = telebot.TeleBot("2105055840:AAHkdn5AeofLhxCD-p9lv_RrUsxKSe67mqM", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, Крошка!") 
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
bot.infinity_polling()