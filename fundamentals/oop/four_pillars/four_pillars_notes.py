#ENCAPSULATION
#grouping chunks of code together so that you can re-use them easily. Every class you build is an exmaple of encapsulation. Every instance of a class can make use of the code inside of the class!

################################

#INHERITANCE
#Occasionally classes are so closely related to other classes that they may take the features of that class, but they are different enough that they can be a class of their own-- so you can create a sub-class that will inherit attributes from the parent-class.

#CELESTIAL BODY - CLASS
#+gravity
#+luminosity

    #PLANET - SUB-CLASS - inherits gravity and luminosity and also has its own attributes
    #+orbit

        #TERRESTRIAL - another level of sub-class. inherit attributes from all parents + have their own
        #made of rock

        #GAS
        #made of gas

        #ICE
        #made of ice

################################

#POLYMORPHISM - a child class can have different versions of a method than the parent class

#MAMMAL
#number of legs = 4
#walk() -> "mammal gallops"

    #HUMAN
    #number of legs = 2
    #walk() -> "huma walks"

    #DOLPHIN
    #number of legs = 0
    #walk() -> "dolphin swims"

#ABSTRACTION - an extension of encapsulation. You can hide attributes or methods that you don't need to look at. You can have things that are called "an abstract class" that you don't instantiate by themselves-- they house information that is too incomplete to exist by itself. i.e., there is no such thing as a generic mammal-- but the overarching theme exists, it's just an abstract idea. So "mammal" would be an abstract class, and wouldn't exist on its own, but is rather used in conjunction with inheritance.