from typing import List

def trapWater(height: List[int]) -> int:
  right = len(height) - 1
  left = 0
  leftMax = rightMax = 0
  amount = 0

  while left < right:
    if height[left] < height[right]:
      if height[left] >= leftMax:
        leftMax = height[left]
      else:
        amount += (leftMax - height[left])
      left += 1
    else:
      if height[right] >= rightMax:
        rightMax = height[right]
      else:
        amount += (rightMax - height[right])
      right -= 1

  return amount

assert trapWater([0,1,0,2,1,0,1,3,2,1,2,1]) == 6