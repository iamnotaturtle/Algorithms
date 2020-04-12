
class Palindrome:
  # Longest Palindrome O(n^2)
  def longestPalindrome(self, s: str) -> str:
    start = 0
    end = 0

    for i in range(0, len(s)):
      len1 = self.expandAroundCenter(s, i, i)
      len2 = self.expandAroundCenter(s, i, i + 1)
      maxLen = max(len1, len2)

      if maxLen > end - start:
        start = i - (maxLen // 2)
        end = i + maxLen // 2

    return s[start : end + 1]

  def expandAroundCenter(self, s: str, i: int, j = int) -> int:
    left = i
    right = j
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return right - left - 1

pal = Palindrome()
print(pal.longestPalindrome('babad'))