class Person:
  def work(self):
    raise NotImplementedError('subclass me')

# Subsystems
class CEO(Person):
  def work(self):
    print('ceo: yell at managers')

class Manager(Person):
  def work(self):
    print('manager: yell at developers')

class Developer(Person):
  def __init__(self, caffiene):
    self.caffeine = caffiene

  def work(self):
    if self.caffeine == 1:
      print('dev: falling asleep...')

    self.caffeine -= 1
    print(f"dev: {'yell' if self.isWorking() else 'yawn'} at screen")

  def isWorking(self):
    return self.caffeine > 0

# Facade
class EfficientCompany:
  def __init__(self):
    self.caffieneStash = 5
    self.ceo = CEO()
    self.manager = Manager()
    self.developer = Developer(10)

  def startDay(self):
    while self.developer.isWorking():
      self.ceo.work()
      self.manager.work()
      self.developer.work()

company = EfficientCompany()
company.startDay()