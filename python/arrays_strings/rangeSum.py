from typing import List

""" 
  Given an immutable array, return the sum from the inclusive range
  Time: O(n) for initialization, O(1) for fetching
  Space: O(n)
"""
class RangeSum:
  def __init__(self, nums: List[int]):
    self.total = [0 for i in range(len(nums) + 1)]
    for i in range(len(nums)):
      self.total[i + 1] = self.total[i] + nums[i]

  def sumRange(self, start: int, end: int) -> int:
    return self.total[end + 1] - self.total[start]


rangeSum = RangeSum([-2, 0, 3, -5, 2, -1])
assert rangeSum.sumRange(0, 2) == 1
assert rangeSum.sumRange(2, 5) == -1
  