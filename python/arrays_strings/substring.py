# Find all substrings of a string
# Time: O(n^3)
def findSubstrings(s: str) -> None:
  i = 0
  while i < len(s):
    j = i + 1
    while j < len(s):
      print(s[i:j])
      j += 1
    i += 1


findSubstrings("abcde")
