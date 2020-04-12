from typing import Dict

# 1:1
# O(n), O(n)
# Space can be O(1) if characters are a subset
def isUnique(s: str) -> bool:
  dict: Dict[str, int]= {}
  for c in s:
    if c in dict:
      return False
    else:
      dict[c] = True
  return True

assert isUnique('abba') == False

# O(n), O(n) (merge sort space complexity)
def isUnique2(s: str) -> bool:
  sorted(s)
  for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
      return False
  return True


assert isUnique2('abba') == False