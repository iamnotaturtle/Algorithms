# O(n) where n is the shorter string
class Solution:
  def oneEditDistance(self, s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
      return False
    
    longer: str = s if len(s) > len(t) else t
    shorter: str = t if len(s) > len(t) else s

    i: int = 0
    j: int = 0
    foundDiff: bool = False

    while i < len(longer) and j < len(shorter):
      if longer[i] != shorter[j]:
        if foundDiff:
          return False
        foundDiff = True

        if len(longer) == len(shorter):
          j += 1
      else:
        i += 1
      j += 1

    return True


  def isOneEditDistanceOptimized(self, s: str, t: str) -> bool:
    ns, nt = len(s), len(t)

    if ns > nt:
      return self.isOneEditDistanceOptimized(t, s)

    if nt - ns > 1:
      return False

    for i in range(ns):
      if s[i] != t[i]:
        if ns == nt:
          return s[i + 1:] == t[i + 1:]
        else:
          return s[i:] == t[i + 1:]
    return ns + 1 == nt

sol = Solution()
assert sol.oneEditDistance("ab", "acb") == True

assert sol.isOneEditDistanceOptimized("cab", "ad") == False