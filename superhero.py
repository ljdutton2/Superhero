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
  '''Add armor to self.armors
    Armor: Armor Object








if __name__ == "__main__":
      ability = Ability("Great Debugging", 50)
      another_ability = Ability("Smarty Pants", 90)
      hero = Hero("Grace Hopper", 200)
      hero.add_ability(ability)
      hero.add_ability(another_ability)
      print (hero.attack())
