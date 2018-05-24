class Dog:
    # It should have the properties name, color, weight
    # It should have the methods bark, eat, sleep
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w

    def bark(self):
        print("Woof!")

    def eat(self):
        print(self.name + " is eating...")

    def sleep(self):
        print(self.name + " is sleeping...")

bingo = Dog("Bingo", "yellow", 10)
spike = Dog("Spike", "white", 8)

print("Bingo's details: ")
print(bingo.name)
print(bingo.color)
print(bingo.weight)

print("\nSpike's details: ")
print(spike.name)
print(spike.color)
print(spike.weight)

print("\nReassigning Spike's weight to 12...")
spike.weight = 12

print("\nSpike's details: ")
print(spike.name)
print(spike.color)
print(spike.weight)

print("\nCreating a new property...")
spike.breed = "Some random breed"
print(spike.breed)

print("\nMake Bingo bark...")
bingo.bark()

print("\nMake Bingo eat...")
bingo.eat()

print("\nMake Spike sleep...")
spike.sleep()
