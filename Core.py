# -*- coding: utf-8 -*-
import telebot
import time
bot = telebot.TeleBot('814941567:AAGu3mHvWgCfqDU1BzzpSg5UEWhVAiKV9D0')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')



@bot.message_handler(commands=['start'])
def start_message(message):
    def botsen(mess):
        bot.send_chat_action(message.chat.id, action='typing')
        time.sleep(1)
        bot.send_message(message.chat.id, mess, reply_markup=keyboard1)
    botsen('Здравствуй путник')
    botsen('Я смотрю ты совсем не помнишь меня')
    botsen('Но это не важно')
    botsen('Ведь я тоже забыл твоё имя')
    botsen('Впрочем')
    botsen('Оно не так важно')
    
    
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
    bot.delete_message(message.chat.id, message.message_id)



bot.polling()