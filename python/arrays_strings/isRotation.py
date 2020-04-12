# O(n^2) time and O(n) space
def isRotation(s: str, target: str) -> bool:
  if len(s) != len(target):
    return False

  target *= 2

  if s in target:
    return True
  else:
    return False

assert isRotation('waterbottle', 'erbottlewat') == True