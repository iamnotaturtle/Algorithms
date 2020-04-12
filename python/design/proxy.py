# Hides implementation details of actual class
from abc import abstractmethod

class AbstractCar:
    @abstractmethod
    def drive(self):
        raise NotImplementedError('whoops')

class Car(AbstractCar):
    def drive(self):
        print('driven')

class Driver:
    def __init__(self, age: int):
        self.age = age
class ProxyCar(AbstractCar):
    def __init__(self, driver):
        self.car = Car()
        self.driver = driver
    
    def drive(self):
        if self.driver.age <= 16:
            print('too young dude')
        else:
            self.car.drive()

driver = Driver(16)
car = ProxyCar(driver)
car.drive()

driver = Driver(25)
car = ProxyCar(driver)
car.drive()