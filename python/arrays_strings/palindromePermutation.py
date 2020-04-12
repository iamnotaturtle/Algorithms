
from typing import Dict

# Time: O(n), Space: O(n)
def isPermutationOfPalindrome(s: str) -> bool:
  count: Dict[str, int] = {}
  countOdd = 0
  for c in s:
    if c not in count:
      count[c] = 1
    else:
      count[c] += 1
    if count[c] % 2 == 1:
      countOdd += 1
    else:
      countOdd -= 1
  return countOdd <= 1

assert isPermutationOfPalindrome("aabcc") == True
assert isPermutationOfPalindrome("aabbcc") == True
assert isPermutationOfPalindrome("abc") == False