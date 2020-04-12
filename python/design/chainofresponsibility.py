"""
This pattern avoids coupling the Sender of a request
to the Receiver
Cocoa Touch classes support this
"""

class Meal:
  isPreping = False
  isCooking = False
  isServing = False

class Kitchen:
  def __init__(self):
    self.handlers = []

  def add(self, handler):
    self.handlers.append(handler)

  def handleMeal(self, meal):
    for handler in self.handlers:
      handler(meal)

# Handlers
def handlePrep(meal):
  meal.isPreping = True
  print('Prepping')

def handleCooking(meal):
  meal.isPreping = False
  meal.isCooking = True
  print('Cooking')

def handleServing(meal):
  meal.isCooking = False
  meal.isServing = True
  print('Serve up!')

handlers = [handlePrep, handleCooking, handleServing]
kitchen = Kitchen()

for handler in handlers:
  kitchen.add(handler)

kitchen.handleMeal(Meal())