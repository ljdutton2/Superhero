import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength


    def attack(self):
        value = random.randint(0, self.max_damage)
        return value


if __name__ == "__main__":
     ability = Ability("Debugging Ability", 20)
     print(ability.name)
     print(ability.attack())



        #''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
