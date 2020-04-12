from typing import List

# O(n), O(1) strings are immutable in python though
def urlify(s: List[str], length: int) -> str:
  i = length - 1
  end = len(s) - 1

  while i >= 0:
    if s[i] == ' ':
      s[end] = '0'
      s[end - 1] = '2'
      s[end - 2] = '%'
      end -= 3
    else:
      s[end] = s[i]
      end -= 1
    i -= 1

  return ''.join(s)

assert urlify(list('Mr John Smith    '), 13) == 'Mr%20John%20Smith'