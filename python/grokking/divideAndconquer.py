def recursiveSum(nums: [int]):
    if len(nums) == 0:
        return 0
    return nums.pop() + recursiveSum(nums)

assert recursiveSum([1,2,3,4,5]) == 15

def recursiveCount(nums: [int]):
    if len(nums) == 0:
        return 0
    return 1 + recursiveCount(nums[1:])

assert recursiveCount([1,1,1]) == 3

def maxNumber(nums: [int]):
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], maxNumber(nums[1:]))

assert maxNumber([6,2,3,4,5]) == 6
    