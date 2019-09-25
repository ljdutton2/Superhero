import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        attack_strength = random.randint(0, self.max_damage)
        return attack_strength


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        value = random.randint(0, self.max_block)
        return value

class Hero:
    def __init__(self, name, starting_health=100):
            self.name = name
            self.starting_health= starting_health
            self.abilities = []
            self.armors =  []
            self.current_health = 100

    def attack(self):
        total_damage = 0
        combine_damage = 0
        for ability in self.abilities:
            combine_damage=Ability.attack(ability)
            total_damage += combine_damage
        return total_damage

    def add_ability(self, ability):
        self.abilities.append(ability)


    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt = 0):
        total_block = 0
        for armor in self.armors:
            total_block += Armor.block(armor)

        return abs(damage_amt - total_block)

#this is running properly but I have no idea how to make sure it subtracts 40
    def take_damage(self,damage):
        damage = self.defend(damage)
        self.current_health -= damage

    def is_alive(self):
        if self.current_health < 1:
            return False
        else:
            return True

    def fight(self,opponent):
        opponent = Hero("Villian")
        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

        if self.is_alive() == False and opponent.is_alive() == False:
            print("Both players are deceased :( ")
        elif self.is_alive():
            print(self.name + " won!")
        else:
            print(opponent.name + " won!")




if __name__ == '__main__':
   hero1 = Hero("Wonder Woman")
   hero2 = Hero("Dumbledore")
   ability1 = Ability("Super Speed", 300)
   ability2 = Ability("Super Eyes", 130)
   ability3 = Ability("Wizard Wand", 80)
   ability4 = Ability("Wizard Beard", 20)
   hero1.add_ability(ability1)
   hero1.add_ability(ability2)
   hero2.add_ability(ability3)
   hero2.add_ability(ability4)
   hero1.fight(hero2)
