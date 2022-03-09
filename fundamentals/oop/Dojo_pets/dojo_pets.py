import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        print("Going for a walk.")
        return self
    def feed(self):
        print("Time for a meal!")
        return self
    def bathe(self):
        print("Let's take a bath now...")
        return self

josh = Ninja("Josh", "Brown", Pet.Cat("Violet", "Cat", "None", "Healthy", "Low energy", "Soft Meow"), "Greenies", "MeowMix")

josh.feed().walk().bathe()