
from dog import Dog

my_dog = Dog("Rex", "Superdog")
print(my_dog.name)
my_dog.bark()

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)
my_other_dog.rollover()

my_moms_dog = Dog("Bodie", "Crocker Spaniel")
print(my_moms_dog.name)
my_moms_dog.sit()
my_moms_dog.bark()


Dog.greeting = ("woah")
