# Abstract Product
class Dog:
    def speak(self):
        pass

# Concrete Products
class Poodle(Dog):
    def speak(self):
        return "Poodle: I'm a poodle dog."

class Husky(Dog):
    def speak(self):
        return "Husky: I'm a husky dog."

# Abstract Factory
class DogFactory:
    def create_dog(self):
        pass

# Concrete Factories
class PoodleFactory(DogFactory):
    def create_dog(self):
        return Poodle()

class HuskyFactory(DogFactory):
    def create_dog(self):
        return Husky()

# Client
def get_dog_speak(dog_factory):
    dog = dog_factory.create_dog()
    return dog.speak()

# Usage example:
poodle_factory = PoodleFactory()
husky_factory = HuskyFactory()

poodle = get_dog_speak(poodle_factory)
print(poodle)  # Output: Poodle: I'm a poodle dog.

husky = get_dog_speak(husky_factory)
print(husky)  # Output: Husky: I'm a husky dog.
