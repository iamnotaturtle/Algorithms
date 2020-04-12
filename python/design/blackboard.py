import abc
import random

  # Blackboard Pattern is used for allowing multiple services to coordinate their work
  # It consists of
  # * blackboard - shared state
  # * knowledge sources - individual contributors
  # * controller - handles sources and blackboard

class Blackboard(object):
  def __init__(self):
    self.experts = []
    self.commonState = {
      'problems': 0,
      'suggestions': 0,
      'contributions': [],
      'progress': 0
    }

  def addExpert(self, expert):
    self.experts.append(expert)

class Controller(object):
  def __init__(self, blackboard):
    self.blackboard = blackboard

  def runLoop(self):
    while self.blackboard.commonState['progress'] < 100:
      for expert in self.blackboard.experts:
        if expert.isEagerToContribute:
          expert.contribute()
    return self.blackboard.commonState['contributions']

class AbstractExpert(object):
  __metaclass__ = abc.ABCMeta

  def __init__(self, blackboard):
    self.blackboard = blackboard

  @abc.abstractclassmethod
  def isEagerToContribute(self):
    raise NotImplementedError('subclass it, son')

  @abc.abstractclassmethod
  def contribute(self):
    raise NotImplementedError('subclass it, son')

class Student(AbstractExpert):
  @property
  def isEagerToContribute(self):
    return True

  def contribute(self):
    self.blackboard.commonState['problems'] += random.randint(1, 10)
    self.blackboard.commonState['suggestions'] += random.randint(1, 10)
    self.blackboard.commonState['contributions'] += [self.__class__.__name__]
    self.blackboard.commonState['progress'] += random.randint(1, 2)

class Scientist(AbstractExpert):
  @property
  def isEagerToContribute(self):
    return random.randint(0, 1)

  def contribute(self):
    self.blackboard.commonState['problems'] += random.randint(10, 20)
    self.blackboard.commonState['suggestions'] += random.randint(10, 20)
    self.blackboard.commonState['contributions'] += [self.__class__.__name__]
    self.blackboard.commonState['progress'] += random.randint(10, 30)

class Professor(AbstractExpert):
  @property
  def isEagerToContribute(self):
    return True if self.blackboard.commonState['problems'] > 100 else False

  def contribute(self):
    self.blackboard.commonState['problems'] += random.randint(1, 2)
    self.blackboard.commonState['suggestions'] += random.randint(10, 20)
    self.blackboard.commonState['contributions'] += [self.__class__.__name__]
    self.blackboard.commonState['progress'] += random.randint(10, 100)

if __name__ == '__main__':
  blackboard = Blackboard()
  blackboard.addExpert(Student(blackboard))
  blackboard.addExpert(Scientist(blackboard))
  blackboard.addExpert(Professor(blackboard))

  controller = Controller(blackboard)
  contributions = controller.runLoop()

  from pprint import pprint
  pprint(contributions)
