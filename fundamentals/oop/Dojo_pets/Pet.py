from turtle import color


class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        print("Nap time...zzzzz")
        return self
    def eat(self):
        print("Mmmmmm... Delicious.")
        return self
    def play(self):
        print("Woohoo! Playtime!")
        return self
    def noise(self):
        print("MEOW!")
        return self

class Cat(Pet):
    def __init__(self, name, type, tricks, health, energy, meow_type):
        super().__init__(name, type, tricks, health, energy)
        self.meow_type = meow_type

class Dog(Pet):
    def __init__(self, name, type, tricks, health, energy, bark_type):
        super().__init__(name, type, tricks, health, energy)
        self.bark_type = bark_type

class Fish(Pet):
    def __init__(self, name, type, tricks, health, energy, salinity):
        super().__init__(name, type, tricks, health, energy)
        self.salinity = salinity