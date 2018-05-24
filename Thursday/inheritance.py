class Animal:
    # It should have the properties name, color, weight
    # It can make_sound
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def make_sound(self):
        print("Unknown sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
        super().make_sound()

    def type_of_animal(self):
        print(self.name + " is a dog")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

    def type_of_animal(self):
        print(self.name + " is a cat")

genericAnimal = Animal("Unknown name", "unknown", 10)
spike = Dog("Spike", "grey", 15)
tom = Cat("Tom", "blue", 12)

genericAnimal.make_sound()
spike.make_sound()
tom.make_sound()

spike.type_of_animal()
tom.type_of_animal()
# genericAnimal.type_of_animal()
