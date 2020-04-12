from typing import List

# Min number of coins for the given amount
def coinChange(coins: List[int], amount: int) -> int:
  lenCoins = len(coins)
  maxAmount = amount + 1
  dp = [maxAmount] * maxAmount
  dp[0] = 0

  for i in range(1, maxAmount):
    for j in range(lenCoins):
      # Coin is less than current amount
      if coins[j] <= i:
        dp[i] = min(dp[i], dp[i - coins[j]] + 1)

  return dp[amount] if dp[amount] <= amount else -1

assert coinChange([1, 2, 5], 11) == 3



def coinChangeRepeating(coins: List[int], amount: int) -> int:
  dp = [0] * (amount + 1)
  dp[0] = 1

  for coin in coins:
    for i in range(1, len(dp)):
      if i >= coin:
        dp[i] += dp[i - coin]
  return dp[amount]

assert coinChangeRepeating([1, 2, 5], 12) == 13