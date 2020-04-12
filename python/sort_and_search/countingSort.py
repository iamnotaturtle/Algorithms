from typing import List

def countingSort(nums: List[int]) -> List[int]:
    results = [0] * len(nums)
    high = max(nums)
    low = min(nums)
    counts = [0 for i in range(low, high + 1)]

    for num in nums:
        counts[num - low] += 1
    
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    
    for num in nums:
        results[counts[num - low] - 1] = num
        counts[num - low] -= 1

    return results


print(countingSort([8, 1, 2, 2, 5]))
assert (countingSort([8, 1, 2, 2, 5])) == [1, 2, 2, 5, 8]