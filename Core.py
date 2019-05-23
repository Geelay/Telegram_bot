# -*- coding: utf-8 -*-
import telebot
import time
from units import *

TOKEN = '814941567:AAGu3mHvWgCfqDU1BzzpSg5UEWhVAiKV9D0'
bot = telebot.TeleBot(TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')
flag = False


@bot.message_handler(commands=['start'])
def start_message(message):
    global flag, HERO
    
    def botsen(mess):
        bot.send_chat_action(message.chat.id, action='typing')
        time.sleep(1)
        bot.send_message(message.chat.id, mess, reply_markup=keyboard1)
    if flag == False:
        flag = True 
        botsen('Здравствуй путник')
        botsen('Я смотрю ты совсем не помнишь меня')
        botsen('Но это не важно')
        botsen('Ведь я тоже забыл твоё имя')
        botsen('Впрочем')
        botsen('Оно не так важно')
        time.sleep(2)
        botsen('')
        HERO = hero
    else:
        pass
    
@bot.message_handler(content_types=[
                                    'text',
                                    'sticker',
                                    'voice',
                                    'audio',
                                    'video',
                                    'photo',
                                    'document',
                                    'venue',
                                    'contact',
                                    'location'
                                    ])
def send_text(message):
    if message.text.lower() == 'готов':
        pass
    else: 
        bot.delete_message(message.chat.id, message.message_id)



bot.polling()