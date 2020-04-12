# Encapsulates the request as an object
class Command:
  def execute(self):
    raise NotImplementedError()

class Light:
  def on(self):
    print("light is on")
    return True

  def off(self):
    print("light is off")
    return False

# Light on request
class LightOnCommand(Command):
  def __init__(self, light):
    self.light = light

  def execute(self):
    return self.light.on()


class Remote:
  def setCommand(self, command):
    self.command = command

  def pressButton(self):
    return self.command.execute()

remote = Remote()
remote.setCommand(LightOnCommand(Light()))
assert remote.pressButton() == True