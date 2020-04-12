# Template methods defined in superclass, implemented in subclass
class AbstractBase():
    def orgMethod(self):
        self.doThis()
        self.doThat()

class Concrete(AbstractBase):
    def doThis(self):
        pass
    def doThat(self):
        pass