
def cyclicalSort(nums: [int]) -> [int]:
    for i, num in enumerate(nums):
        nums[i], nums[num - 1] = nums[num - 1], nums[i]
    return nums

assert cyclicalSort([6, 3, 5, 2, 4, 1]) == [1, 2, 3, 4, 5, 6]