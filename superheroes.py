import random
# Lauren todo fix pytest
# super function


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
            self.starting_health = starting_health
            self.abilities = []
            self.armors = []
            self.kills = 0
            self.deaths = 0
            self.current_health = starting_health
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.kills += num_deaths

    def attack(self):
        total_damage = 0
        combine_damage = 0
        for ability in self.abilities:
            combine_damage = Ability.attack(ability)
            total_damage += combine_damage
        return total_damage

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt=0):
        total_block = 0
        for armor in self.armors:
            total_block += Armor.block(armor)

        return abs(damage_amt - total_block)

# this is running properly but I have no idea how to make sure it subtracts 40
    def take_damage(self, damage):
        damage = self.defend(damage)
        self.current_health -= damage

    def is_alive(self):
        if self.current_health < 1:
            return False
        else:
            return True

    def fight(self, opponent):
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
        # super() function

    def attack(self, other_team):
        weapon_attack = self.max_damage // 2
        return (random.randint(weapon_attack, self.max_damage))


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        return self.heroes.remove(hero)

    def viewallheroes(self):
        for hero in self.heroes:
            print(hero.name)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            print(hero.name)
            print(f"Kills: {hero.kills}  Deaths: {hero.deaths}.")

    def attack(self, other_team):
        hero_attackers = []
        opponent_attackers = []

        for hero in self.heroes:
            if hero.is_alive() == True:
                hero_attackers.append(hero)

        for hero in other_team.heroes:
            if hero.is_alive() == True:
                opponent_attackers.append(hero)

        while len(hero_attackers) > 1 and len(opponent_attackers):
            hero_fighter = random.choice(hero_attackers)
            opponent_fighter = random.choice(opponent_attackers)
            hero_fighter.fight(opponent_fighter)
            if not hero_fighter.is_alive(): hero_attackers.pop(hero_fighter)
            if not opponent_fighter.is_alive(): opponent_attackers.pop(opponent_fighter)




class Arena:

    def __init__(self):
        self.con()

    def con(self):
        self.team_one = self.build_team_one()
        self.team_two = self.build_team_two()

    def create_ability(self):
        ability_1 = input("Choose an ability for your hero")
        ability_max = input(f"What is the max damage of {ability_1}: ")
        user_ability = Ability(ability_1, ability_max)
        return user_ability


    def create_weapon(self):
        weapon_1 = input("Choose a weapon for your hero")
        weapon_max = input(f"What is the max damage of {weapon_1}: ")
        user_weapon = Weapon(weapon_1, weapon_max)
        return user_weapon


    def create_armor(self):
        armor_1 = input("Choose an armor to protect your hero")
        armor_max = input(f"What is the max protection of the {armor_1}: ")
        user_armor = Armor(armor_1, armor_max)
        return user_armor


    def create_hero(self):
        hero_name = input("Choose a name for your hero!")
        new_hero = Hero(hero_name)
        abilities = self.create_ability()
        armors = self.create_armor()
        weapons = self.create_weapon()
        new_hero.add_ability(abilities)
        new_hero.add_armor(armors)
        new_hero.add_weapon(weapons)
        return new_hero


    def build_team_one(self):
        team_1_name = input("Choose a name for Team 1")
        first_team = Team(team_1_name)
        team_1_heroes = int(input(f"How many heroes are on {team_1_name}? "))
        for _ in range(team_1_heroes):
            hero = self.create_hero()
            first_team.add_hero(hero)
        return first_team

    def build_team_two(self):
        team_2_name = input("Choose a name for Team 2")
        second_team = Team(team_2_name)
        team_2_heroes = int(input(f"How many heroes are on {team_2_name}? "))
        for _ in range(team_2_heroes):
            hero = self.create_hero()
            second_team.add_hero(hero)
        return second_team


    def team_battle(self):
        print("Let the battle begin!")
        #error
        self.team_one.attack(self.team_two)

    def show_stats(self):
        # need to add winning team
        # add k/d
        # show surviving heroes
        print("The results are: ")
        team_1_result = self.team_one.stats()
        team_2_results = self.team_two.stats()
        print(team_1_result)
        print(team_2_results)



if __name__ == '__main__':
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
