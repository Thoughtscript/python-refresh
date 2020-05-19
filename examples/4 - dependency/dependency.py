# dependency example (for injection into example_one.py)
## note that filenames don't have to align with classes (this is less clear in Django)

class Dog:
    breed = "grayhound"
    name = "fido"


# multiple classes in one script
class Cat:

    # constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # instance method
    def meow(self, meow):
        ## string interpolation
        return "{} says meow {}".format(self.name, meow)

# executable code
cat = Cat("Sonata", "black cat")
print(cat.meow("meow"))

class RoboCat(Cat):

    # constructor with super
    def __init__(self, name, breed, metal):
        super().__init__(name, breed)
        self.metal = metal
