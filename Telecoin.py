# -*- coding: utf8 -*-
import telebot
import time
import json
import random
from telebot import types
bot = telebot.TeleBot('5729089320:AAHHI_2aIlLAnK5POnGu28QvmBZ5LMVm-7w')
@bot.message_handler(commands=["start"])
def start(message, res=False):
    
    with open('bd_telebot.json', 'r') as file:
        data = json.load(file)
    idtg = str(message.from_user.id)
    if idtg not in data:
        with open('bd_telebot.json', 'r') as file:
            data = json.load(file)
        name = str(message.chat.first_name)
        idtg = str(message.from_user.id)
        i = 1

        rbr = {"idcoin": i, "name": name, "tgcoins" : 0, "email": None, "token": None, "nikname": None}
        data[idtg] = rbr
        with open('bd_telebot.json', 'w') as file:
            json.dump(data, file, indent=4)
        i += 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
    btn1 = types.KeyboardButton("Кошелек")
    btn2 = types.KeyboardButton('Профиль🙍‍♂')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Готово',  reply_markup=markup)
bot.polling(none_stop=False)