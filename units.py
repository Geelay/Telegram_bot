import random

class item:
    _image = None
    _health = None
    _defence = None
    _speed = None
    _dexterity = None
    _strength = None
    _constitution = None
    _intelligence = None
    _wisdom = None
    _charisma = None

    def equip(self, target):
        target._health += self._health
        target._defence += self._defence
        target._speed += self._speed
        target._dexterity += self._dexterity
        target._strength += self._strength
        target._constitution += self._constitution
        target._intelligence += self._intelligence
        target._wisdom += self._wisdom
        target._charisma += self._charisma

    def unequip(self, target):
        target._health -= self._health
        target._defence -= self._defence
        target._speed -= self._speed
        target._dexterity -= self._dexterity
        target._strength -= self._strength
        target._constitution -= self._constitution
        target._intelligence -= self._intelligence
        target._wisdom -= self._wisdom
        target._charisma -= self._charisma
    
class Normal_unit:

    _image = None
    _health = None
    _defence = None
    _name = None
    _exp = None
    _race = None
    _speed = None
    _dexterity = None
    _strength = None
    _constitution = None
    _intelligence = None
    _wisdom = None
    _charisma = None

    def attack(self, target):
        target._health -= self._attack
        print(target.name, target._health, '/', target._healthfull, 'HP')

    def is_alive(self):
        return self._health > 0

class Bandit(Normal_unit):
    _health = 11
    _defence = 12
    _name = 'Bandit'
    _exp = 25
    _race = 'Humanoid'
    _speed = 30
    _dexterity = 12
    _strength = 11
    _constitution = 12
    _intelligence = 10
    _wisdom = 10
    _charisma = 10

    def scimilar(self, target): #Melee weapon attack
        target._slashing = True
        target._health -= 1 + random.randint(0, 6)

    def light_crossbow(self, target): #Ranged weapon attack
        target._piercing = True
        target._health -= 1 + random.randint(0, 8)

class Blood_hawk(Normal_unit):
    pass

class Boggle(Normal_unit):
    pass

class Camel(Normal_unit):
    pass

class Cultist(Normal_unit):
    pass

class Flumph(Normal_unit):
    pass

class Giant_rat(Normal_unit):
    pass

class Giant_crab(Normal_unit):
    pass

class Kobold(Normal_unit):
    pass

class Manes(Normal_unit):
    pass

class Merfolk(Normal_unit):
    pass



class Elite_unit:
    _health = None
    _attack = None

    def attack(self, target):
        target._health -= self._attack
        print(target.name, target._health, '/', target._healthfull, 'HP')

    def is_alive(self):
        return self._health > 0


class Boss:
    _health = None
    _attack = None

    def attack(self, target):
        target._health -= self._attack
        print(target.name, target._health, '/', target._healthfull, 'HP')

    def is_alive(self):
        return self._health > 0


class Hero:


    _image = None
    _health = None
    _defence = None
    _name = None
    _exp = None
    _race = None
    _speed = None
    _dexterity = None
    _strength = None
    _constitution = None
    _intelligence = None
    _wisdom = None
    _charisma = None
    _class = None   
    _lvl = None

    def attack(self, target):
        target._health -= self._attack
        print(target.name, target._health, '/', target._healthfull, 'HP')

    def is_alive(self):
        return self._health > 0


