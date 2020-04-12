# Two classes want to talk to each other
# Have different interfaces
# Use adapter to expose the adaptee to the other class

# First example
class Adaptee:
  def specificRequest(self):
    return "Adaptee"

class Adapter:
  def __init__(self, adaptee):
    self.adaptee = adaptee

  def request(self):
    return self.adaptee.specificRequest()

client = Adapter(Adaptee())
print(client.request())

# Second Example
class UppercasingFile:
  def __init__(self, *a, **k):
    self.f = open(*a, **k)

  def write(self, data):
    self.f.write(data.upper())

  def close(self):
    self.f.close()

file = UppercasingFile('test.txt', 'w+')
file.write('hey')
file.close()
