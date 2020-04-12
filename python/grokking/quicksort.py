def quicksort(nums: [int]):
    if len(nums) < 2:
        return nums
    
    pivot = nums[0]
    less = [i for i in nums[1:] if i <= pivot]
    greater = [i for i in nums[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

def partition(nums: [int], start: int, end: int):
    pivot = nums[start]
    high = end
    low = start + 1

    while True:
        while low <= high and nums[high] >= pivot:
            high -= 1
        while low <= high and nums[low] <= pivot:
            low += 1

        if low <= high:
            nums[low], nums[high] = nums[high], nums[low]
        else:
            break

    # Swap pivot
    nums[start], nums[high] = nums[high], nums[start]

    return high

def qsort(nums: [int], start: int, end: int):
    if start >= end:
        return nums
    p = partition(nums, start, end)
    qsort(nums, start, p - 1)
    qsort(nums, p + 1, end)

    return nums

ar = [2,8,1,5]
ar2 = [10,8,3,4,7]
print(quicksort(ar))
print(qsort(ar2, 0, len(ar2) - 1))
# 1 2 5 8
            