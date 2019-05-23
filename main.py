# coding: utf-8
from units import *
def battle(hero, villain, hero_action, villain_action):
    h_speed = hero._speed
    v_speed = villain._speed
    if h_speed > v_speed:
        hero_action
    elif v_speed > h_speed:
        villain_action
    else:
        hero_action
        villain_action
sword = Shortsword()
HERO = Traveler( 40, 8, 'Geelay', 0, 20, 8, 8, 8, 8, 8,8)
sword.equip(HERO)
bandit = Bandit()
print(bandit._health)
print(HERO._health)
battle(HERO, bandit, sword.light_atack(HERO, bandit), bandit.scimilar(HERO))
print(bandit._health)
print(HERO._health)