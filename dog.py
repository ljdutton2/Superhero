class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woof!!")
my_dog = Dog("Rex", "Superdog")
my_dog.bark()
