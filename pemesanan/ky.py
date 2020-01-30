# -*- coding: utf-8 -*-
"""
This Example will show you how to use register_next_step handler.
"""

import telebot
from telebot import types

API_TOKEN = '1047466776:AAFcmsGjZ18mE1YvKgCdVXqT5X6CYKOYtxs'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.panganan = None
        self.minuman = None
       


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    cid = message.chat.id
    msg = bot.reply_to(message,'Halo, Saya sufi_bot. Selamat Datang Diwarung Mie Ayam Bakso Mang Ujang')
    msg = bot.send_message(cid ,'Siapa Nama Anda?')
    
    bot.register_next_step_handler(msg, process_name_step)
   


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user  
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Bakso','Mie Ayam','Mie Ayam Bakso')
        msg = bot.reply_to(message, user.name+ '. Makanan apa yang ingin anda pesan?',reply_markup=markup)
        bot.register_next_step_handler(msg, process_panganan_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')
        


def process_panganan_step(message):
    try:
        chat_id = message.chat.id
        panganan = message.text
        hargamakan = message.text
        user = user_dict[chat_id]
        if (panganan == u'Bakso'):
            user.hargamakan = 10000
            user.panganan = panganan
        elif (panganan == u'Mie Ayam'):
            user.hargamakan = 7000
            user.panganan = panganan
        elif (panganan == u'Mie Ayam Bakso'):
            user.hargamakan = 15000
            user.panganan = panganan

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Es Teh', 'Es Jeruk')
        msg = bot.reply_to(message, 'Pilih Minuman yang mana?',reply_markup=markup)
        bot.register_next_step_handler(msg,process_minuman_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_minuman_step(message):
    try:
        chat_id = message.chat.id
        minuman = message.text
        hargaminum = message.text
        user = user_dict[chat_id]
        if (minuman == u'Es Teh'): 
            user.hargaminum = 2500
            user.minuman = minuman
        elif (minuman == u'Es Jeruk') :
            user.hargaminum = 4000
            user.minuman = minuman
        else:
            raise Exception()
        bot.send_message(chat_id, 'List Pesanan : \n' +'Nama pemesan = ' +user.name+ '\n Makanan yang dipesan :' +user.panganan+ ' harga = '+str(user.hargamakan)+  '\n Minuman yang dipesan :'+user.minuman+' harga =  ' +str(user.hargaminum)+ '\n Total harga = {}'.format(user.hargaminum+user.hargamakan) )
        bot.send_message(chat_id,'\n Terima kasih telah makan di Warung Mie Ayam Bakso mang Ujang')
        
    except Exception as e:
        bot.reply_to(message, 'oooops')
        


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

bot.polling()