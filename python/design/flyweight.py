# Main objective is to reduce number of objects

# Heavy object
class CodingPlatform:
  def __init__(self, language):
    self.language = language

class PlatformFactory:
  def __init__(self):
    self.platforms = {}

  def getPlatform(self, language):
    if language not in self.platforms:
      self.platforms[language] = CodingPlatform(language)
    return self.platforms[language]

factory = PlatformFactory()
cPlatform = factory.getPlatform('c')
cPlatform2 = factory.getPlatform('c') # Same object

assert len(factory.platforms) == 1
