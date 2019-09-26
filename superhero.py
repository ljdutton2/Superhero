import random
#Lauren todo fix pytest
#super function 

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
#I dont understand how/why we can make self variables if its not a paramater in init
            self.deaths = 0
            self.kills = 0

    def add_kills(self,num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.kills += num_deaths



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
            # is this redundant
            self.add_kills(1)
            opponent.add_deaths(1)
            print(self.name + " won!")
        else:
            self.add_deaths(1)
            opponent.add_kills(1)
            print(opponent.name + " won!")

class Weapon(Ability):
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        #super() function
    def attack(self):
        weapon_attack = self.max_damage // 2
        return (random.randint(weapon_attack, self.max_damage))


class Team:
    def __init__(self,name,):
        self.name = name

    def add_hero(self,hero):
        hero_list = self.hero = []
        hero_list.append(hero)

    def remove_hero(self,hero):
        return hero_list.remove(hero)

    def viewallheroes(self):
        for hero in self.hero:
            print(hero.name)






if __name__ == '__main__':
    knife = Weapon("knife", 30)
    print(knife.name)
    print(knife.attack())
