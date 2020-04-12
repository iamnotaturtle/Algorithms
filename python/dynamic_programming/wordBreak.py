from typing import List, Set

def wordBreak(s: str, wordDict: List[str]) -> bool:
  wordDictSet = set(wordDict)
  n = len(s)
  dp: List[bool] = [False] * (n + 1)
  dp[0] = True

  for i in range(n + 1):
    for j in range(i):
      if dp[j] and s[j : i] in wordDictSet:
        dp[i] = True
        break
  return dp[n]

print(wordBreak("leetcode", ["leet","code"]))