import telebot
import time
from units import *

TOKEN = '814941567:AAGu3mHvWgCfqDU1BzzpSg5UEWhVAiKV9D0'
bot = telebot.TeleBot(TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')
flag = False
flag1 = True
NUMBER = 1



def battle(hero, villain, hero_action, villain_action):
    h_speed = hero._speed
    v_speed = villain._speed
    time.sleep(2)
    if h_speed > v_speed:
        hero_action
        bot.send_message('-1001253900604', 'Вы: ' + str(hero._health) + '\n' + villain._name + str(villain._health) , reply_markup=keyboard1)
        h_speed -= v_speed
        v_speed = villain._speed
    elif v_speed > h_speed:
        villain_action
        bot.send_message('-1001253900604', 'Вы: ' + str(hero._health) + '\n' + villain._name + str(villain._health) , reply_markup=keyboard1)
        v_speed -= h_speed
        h_speed = hero._speed
    elif v_speed == h_speed:
        hero_action
        villain_action
        bot.send_message('-1001253900604', 'Вы: ' + str(hero._health) + '\n' + villain._name + str(villain._health) , reply_markup=keyboard1)



@bot.message_handler(commands=['start'])
def start_message(message):
    global flag, HERO, item, NUMBER, flag1, sword
    
    def botsen(mess):
        bot.send_chat_action(message.chat.id, action='typing')
        time.sleep(1)
        bot.send_message(message.chat.id, mess, reply_markup=keyboard1)
    if flag == False:
        flag = True 
        f = open('Base.txt', 'a')
        f.write(str(message.from_user.id)+ ', ' + str(NUMBER)+ '\n')
        NUMBER += 1
        HERO = Traveler(40, 8, 'Geelay', 0, 20, 8, 8, 8, 8, 8, 8, 1)
        botsen('Здравствуй путник')
        botsen('Я смотрю ты совсем не помнишь меня')
        botsen('Но это не важно')
        botsen('Ведь я тоже забыл твоё имя')
        botsen('Впрочем')
        botsen('Оно более не имеет значения')
        botsen('В любом случае я пока не могу ответить на твои вопросы, тебя ждут в другом месте')
        botsen('Однако, я не могу отпустить тебя туда одного')
        time.sleep(2)
        sword = Shortsword('Благословенный подарок')
        sword.equip(HERO)
        with open (sword._image, 'rb') as photo:
            item = bot.send_photo(message.chat.id, photo, sword._name, reply_markup=keyboard1)
        botsen('Ах да, забыл')
        botsen('В этом теле у тебя нет рук')
        keyboard1.add(*[telebot.types.KeyboardButton('Возьмись')])
        botsen('Попробуй сказать "Возьмись"')
        flag1 = False

        
        f.close()
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
    global HERO, item, flag1, sword, bandit, bann
    if flag1 == False:
        flag1 == True
        if message.text.lower() == 'возьмись':
            bot.delete_message(message.chat.id, item.message_id)
            def botsen(mess):
                bot.send_chat_action(message.chat.id, action='typing')
                time.sleep(1)
                bot.send_message(message.chat.id, mess, reply_markup=keyboard1)
            botsen('Забавно')
            botsen('Не думал что это сработает')
            botsen('Раз уж ты обладаешь такой силой, не стоит тебя больше задерживать')
            botsen('Попробуй произнести это заклинание на языке старших эльфов')
            botsen('https://t.me/joinchat/EaGnmxc9MxLX9zfktv7v6A')
            bot.send_message('-1001253900604' , 'ГЛУПЕЦ, ТЫ ДУМАЛ ЧТО БУДЕТ НАСТОЛЬКО ПРОСТО?', reply_markup=keyboard1)
            time.sleep(1)
            bot.send_message('-1001253900604' , '*говори "атака" для обычной атаки врагов, в будующем тебе будут доступны больше умений*', reply_markup=keyboard1)
            bandit = Bandit()
            with open (bandit._image, 'rb') as photo:
                bann = bot.send_photo('-1001253900604', photo, bandit._name, reply_markup=keyboard1)

                

        if message.text.lower() == 'атака':
            while bandit._health > 0:
                battle(HERO, bandit, sword.light_atack(HERO, bandit), bandit.scimilar(HERO))
            bot.delete_message('-1001253900604', bann.message_id)
            bot.send_message('-1001253900604' , 'ДУМАЕШЬ НА ЭТОМ ТВОИ СТРАДАНИЯ ЗАКОНЧАТСЯ?', reply_markup=keyboard1)
            HERO._health = 1000
            while HERO._health > 0:
                enemy = random.choice(enemy_types) 
                with open (enemy._image, 'rb') as photo:
                    bann = bot.send_photo('-1001253900604', photo, enemy._name, reply_markup=keyboard1)
                if enemy._name == 'Boggle':
                    atk = enemy.pummel(HERO)
                if enemy._name == 'Bandit':
                    atk = enemy.scimilar(HERO)
                if enemy._name == 'Blood Hawk':
                    atk = enemy.beak(HERO)
                while enemy._health > 0:
                    battle(HERO, enemy, sword.light_atack(HERO, enemy), atk)
                bot.delete_message('-1001253900604', bann.message_id)
                
            
            
        else:
            bot.delete_message(message.chat.id, message.message_id)
    else:
        bot.delete_message(message.chat.id, message.message_id)




bot.polling()
