import random

class Cat:
  def speak(self):
    return "meow"

  def __str__(self):
    return "Cat"

class Dog:
  def speak(self):
    return "woof"

  def __str__(self):
    return "Dog"

class CatFactory:
  def getPet(self):
    return Cat()

  def getFood(self):
    return "Cat Food"

class DogFactory:
  def getPet(self):
    return Dog()

  def getFood(self):
    return "Dog Food"

# Abstact Factory
class PetShop:
  def __init__(self, animalFactory = None):
    self.animalFactory = animalFactory

  def showPet(self):
    pet = self.animalFactory.getPet()
    print("This is a lovely pet", pet)
    print("It says", pet.speak())
    print("It eats", self.animalFactory.getFood())

# Demo
def getFactory():
  return random.choice([DogFactory, CatFactory])()

shop = PetShop()
for i in range(3):
  shop.animalFactory = getFactory()
  shop.showPet()
  print("=" * 10)