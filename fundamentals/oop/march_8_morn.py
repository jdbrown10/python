# any time you're calling on a built-in data-type or function, you're essentially using object-oriented programming
# ie, the array class is what dictates the rules that arrays follow. And each individual array you create is an instance of the array "blueprint"--they all follow the same set of rules, and you have a bunch of methods that will work with those arrays
#the goal of OOP is to create chunks of code that we can re-use
#big three parts: Classes, Attributes, Methods

#CLASSES
#A class is like a blueprint. The structure that is always the same for each instance. If you think of people: we are all instances of the "human" class, but on an individual level we are unique. It's a very broad outline of a thing.
#To declare a class, call on keyword of "class". the class itself is uppercase and singular.
#pass is a keyword that is for an empty codeblock. It's like a placeholder.
#Attributes and methods are housed inside of a classes.

class Dog:
    pass

#these are 3 unique instances of the "Dog" class. They each get their own memory location because they ultimately get quite complex once you give them attributes and methods.
spike = Dog()
fido = Dog()
brutus = Dog()

print(spike)
print(fido)
print(brutus)

#ATTRIBUTES
#Characteristics shared by all instances of a class type. They don't necessarily have to have the same value from instance to instance. (i.e. fur color--every dog has one, but it's not always the same color). Or, you can have a certain number of windows on a house, or a unique street address, or the material it's built from.
#The init function says "this is how the blueprint creates instances based on the class"
#The SELF keyword (there is equivalence of this in every language... in JS, it's "this". It allows an instance to refer to itself.) You always need to use the self keyword when you're building instances of a class. The init function is inherently called whenever you create an instance of a class (anytime you create a Dog, the init function within the blueprint is called.)
#This example hard codes the values into the attributes, so every instance is the same. 

class Dog:
    def __init__(self):
        self.name = "Fido"
        self.breed = "Golden Retriever"
        self.age = 4
        self.personality_type = "Mellow"

#If you DIDN'T want every Dog to have all of the same attribute values, you'd need to be able to pass data into them rather than hard coding them.
#For example:


class Dog:
    def __init__(self, dog_name): #because Python is loosely typed, you don't have to specify the data type here
        self.name = dog_name
        self.breed = "Golden Retriever"
        self.age = 4
        self.personality_type = "Mellow"

spike = Dog("Spike")
fido = Dog("Fido")
brutus = Dog() #this will not work anymore, because the class now requires the name attribute as an input

print(spike.dog_name) #THIS doesn't work!!! Because "dog_name" it's a parameter for the class
print(spike.name) #THIS works because it's an attribute within the class (where it says "self.name on line 43")


#another way to do this is by allowing the class to accept Data, and have all of that data stored inside of its own box
#i.e.:

class Dog:
    def __init__(self, data): 
        self.name = data["name"]
        self.breed = data["breed"]
        self.age = data["age"]
        self.personality_type = data["p_type"]
        self.energy_level = 100

spike_data = {
    "name" : "Spike",
    "breed" : "Golden Doodle",
    "age" : 5,
    "p_type" : "Mellow"
}

#Class attributes-- attributes not initialized with the "self" keyword. They don't go inside the init method--they get attached to the class. They're the same thing throughout and every instance has the same value. It can be overridden within an instance.

class Dog:
    is_mammal = True #class attribute
    surname = "SuperSnoot" #class attribute
    all_dog_names = [] #this will collect the name from every Dog instance (line 84)
    def __init__(self, data):
        self.name = data["name"]
        self.breed = data["breed"]
        self.age = data["age"]
        self.personality_type = data["p_type"]
        Dog.all_dog_names.append(self.name) #adds the name of every instance of a Dog every time one is initialized and stores it at the class level

#Methods-- you must ALWAYS pass "self" into an instanced method

#this method uses an f string to allow any Dog to use its own name when it calls on this method
def go_for_a_walk(self):
    self.energy_level = self.energy_level - 5
    print(f"My name is {self.name} and my owner took me for a stroll! Now my energy level is {self.energy_level}!")

def take_a_nap(self):
    self.energy_level = 100
    print("zzzzzzzzzzz...")

spike.go_for_a_walk() #drops spike's energy level by 5
spike.go_for_a_walk()
spike.go_for_a_walk()
spike.go_for_a_walk()
spike.go_for_a_walk()
spike.go_for_a_walk()
spike.go_for_a_walk()
spike.take_a_nap() #back to 100