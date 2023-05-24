
class Character:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, other):
        damage = self.strength - other.defense
        if damage > 0:
            other.health -= damage
            print(f"{self.name} attacked {other.name} and dealt {damage} damage!")
        else:
            print(f"{self.name}'s attack was ineffective against {other.name}.")

class Player(Character):
    def __init__(self, name, health, strength, defense):
        super().__init__(name, health, strength, defense)
        self.experience = 0
        self.level = 1

    def level_up(self):
        self.level += 1
        self.health += 10
        self.strength += 5
        self.defense += 5
        print(f"{self.name} has leveled up to level {self.level}!")

class Enemy(Character):
    def __init__(self, name, health, strength, defense):
        super().__init__(name, health, strength, defense)
        self.gold = 10

    def drop_gold(self):
        return self.gold

player = Player("John", 100, 20, 10)
enemy = Enemy("Orc", 80, 15, 5)

while player.health > 0 and enemy.health > 0:
    player.attack(enemy)
    if enemy.health > 0:
        enemy.attack(player)

if enemy.health <= 0:
    player.experience += 50
    enemy.drop_gold()
    print(f"{player.name} defeated {enemy.name} and gained 50 experience and {enemy.drop_gold()} gold!")

    if player.experience >= 100:
        player.level_up()
else:
    print(f"{player.name} was defeated by {enemy.name}. Game over.")
