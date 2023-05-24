from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    STUN = 5
    GUARD_FOR_ALL = 6
    REVIVE = 7
    INVISIBILITY = 8
    RESET = 4




class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        if hero.health <= 0:
            self.choose_defence(heroes)
        else:
            self.__defence = hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        if not isinstance(super_ability, SuperAbility):
            raise ValueError("Ability must be of type SuperAbility")
        else:
            self.__super_ability = super_ability

    def hit(self, boss):
        boss.health = boss.health - self.damage

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeffient = randint(2, 5)
        boss.health = boss.health - self.damage * coeffient
        print(f'Warrior hits critically: {self.damage * coeffient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage = hero.damage + int(hero.damage * 0.25)
        print('Power of each heroes was increased!')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health = hero.health + self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damaged = 0

    def apply_super_power(self, boss, heroes):
        self.health = self.health - int(boss.damage * 0.95)
        self.__saved_damaged = int(boss.damage * 0.05)
        self.damage = self.damage + self.__saved_damaged
        print("Berserk's power was increased")

class Thor(Hero):
    def __init__(self, name, health, damage):
        super(Thor, self).__init__(name, health, damage, SuperAbility.STUN)

    def apply_super_power(self, boss, heroes):
        stun_chance = randint(1, 11)
        if stun_chance == 3:
            print('Boss has been stunned')
            for hero in heroes:
                hero.health = hero.health + boss.damage

class Golem(Hero):
    def __init__(self, name, health, damage):
        super(Golem, self).__init__(name, health, damage, SuperAbility.GUARD_FOR_ALL)

    def apply_super_power(self, boss, heroes):
        self.health = self.health - (boss.damage + int(boss.damage * 0.8))
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health = hero.health + int(boss.damage * 0.2)
        print('GUARDED!')

class Withcer(Hero):
    def __init__(self, name, health, damage=0):
        super(Withcer, self).__init__(name, health, damage, SuperAbility.REVIVE)
        if damage > 0:
            raise ValueError('Damage must be 0 for this hero!')

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0 and hero != self and self.health > 0:
                hero.health = self.health
                self.health = 0
                print('Hero was revived')

class TimeLord(Hero):
    def __init__(self, name, health, damage=0):
        super().__init__(self, name, health, damage, SuperAbility.RESET)
        if damage > 0:
            raise ValueError('Damage must be 0 for this hero too!')

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0


round_counter = 0


def print_statistics(boss, heroes):
    print('ROUND ' + str(round_counter) + ' -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0 and boss.health > 0:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Volendemort', 1000, 60)
    warrior = Golem('Billy', 440, 10)
    doc = Medic('Rimuru', 260, 4, 10)
    berserk = Withcer('Geralt', 240)
    magic = Magic('Steve', 270, 20)
    assistant = TimeLord('Tardis', 350, 40)
    heroes = [warrior, doc, berserk, magic, assistant]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
