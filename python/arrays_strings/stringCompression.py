# Time: O(n), need to traverse full word, O(n) space
def compress(s: str) -> str:
  result = ''
  
  i = 0
  length = len(s)
  while i < length:
      key = s[i]
      count = 0
      while i < length and key == s[i]:
        count += 1
        i += 1
      result += f'{key}{count}'
  
  return result if len(result) < length else s

assert compress('aabcccccaaa') == 'a2b1c5a3'