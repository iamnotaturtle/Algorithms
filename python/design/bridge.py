# Consists of abstraction, refined abstraction
# implementor and concrete implementor
# Refined abstraction contains reference to implementor

# Abstraction
class Instrument:
  def play(self):
    pass

  def tune(self):
    pass

# Refined Abstraction
class Guitar(Instrument):
  def __init__(self, guitarAPI):
    self.guitarAPI = guitarAPI

  def play(self):
    self.guitarAPI.play()

# Implementor
class GuitarAPI:
  def play(self):
      pass

# ConcreteImplementor 1/2
class ClassicalAPI(GuitarAPI):
  def play(self):
    print("Playing some Bach")

# ConcreteImplementor 2/2
class MetalAPI(GuitarAPI):
  def play(self):
    print("Playing some Hu Hu Hu")

instruments = [
  Guitar(ClassicalAPI()),
  Guitar(MetalAPI())
]

for instrument in instruments:
  instrument.play()