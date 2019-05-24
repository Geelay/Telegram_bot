from units import *
import time

def battle(hero, villain, hero_action, villain_action):
    global num
    h_speed = hero._speed
    v_speed = villain._speed

    time.sleep(2)
    num += 1
    print('Раунд ' + str(num) )
    if h_speed > v_speed:
        hero_action
        print('Вы: ' + str(hero._health) + '\n' + villain._name +' '+ str(villain._hhealth) )
        h_speed -= v_speed
        v_speed = villain._speed
    elif v_speed > h_speed:
        villain_action
        print( 'Вы: ' + str(hero._health) + '\n' + villain._name +' '+ str(villain._health) )
        v_speed -= h_speed
        h_speed = hero._speed
    elif v_speed == h_speed:
        hero_action
        villain_action
        print( 'Вы: ' + str(hero._health) + '\n' + villain._name +' '+ str(villain._health) )
        
sword = Shortsword('х')
HERO = Traveler(40, 8, 'Geelay', 0, 20, 8, 8, 8, 8, 8, 8, 1)
sword.equip(HERO)
bandit = Bandit()
while bandit._health > 0:
    battle(HERO, bandit, sword.light_atack(HERO, bandit), bandit.scimilar(HERO))