from typing import List

# Peeks and Valleys. O(n) time, O(1) space
def maxProfitPeeksValleys(prices: List[int]) -> int:
  if not prices:
    return 0

  maxProfit = 0
  minPrice = prices[0]

  for i in range(1, len(prices)):
    minPrice = min(prices[i], minPrice)
    maxProfit = max(prices[i] - minPrice, maxProfit)

  return maxProfit

assert maxProfitPeeksValleys([7, 1, 5, 3, 6, 4]) == 5
