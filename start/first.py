import telebot

API_TOKEN = '1047466776:AAFcmsGjZ18mE1YvKgCdVXqT5X6CYKOYtxs'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Halo, Saya ChatBot. Ada yang bisa saya bantu")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.polling()