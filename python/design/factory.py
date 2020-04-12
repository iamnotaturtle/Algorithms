class Monster(object):
  def __init__(self):
    self.power = None

  def attack(self):
    return self.power

class DragonMonster(Monster):
  def __init__(self):
    self.power = 'fire breath'

class GraveHagMonster(Monster):
  def __init__(self):
    self.power = 'tongue slash'

class MonsterFactory(object):
  @staticmethod
  def createMonster(type):
    if type == 'dragon':
      return DragonMonster()
    if type == 'mourntart':
      return GraveHagMonster()

for monster in ('dragon', 'mourntart'):
  print(f"{monster} attacks with {MonsterFactory.createMonster(monster).attack()}")
