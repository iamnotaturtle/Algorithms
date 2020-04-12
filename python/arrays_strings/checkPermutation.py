from typing import Dict

# 1:2
# Time: O(n + m), Space: O(n + ms)
def isPermutation(s1: str, s2: str) -> bool:
  if len(s1) != len(s2):
    return False

  dict: Dict[str, int] = {}

  for c in s1:
    dict[c] = 1 if c not in dict else dict[c] + 1
  
  for c in s2:
    if c not in dict:
      return False
    dict[c] -= 1

    if dict[c] < 0:
      return False
  
  return True

assert isPermutation("abbc", "cbba") == True
assert isPermutation("abc", "abbda") == False