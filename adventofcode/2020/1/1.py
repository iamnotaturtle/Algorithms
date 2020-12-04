import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')
file = open(file_path, 'r')

lines = file.readlines()
nums = [int(x) for x in lines]

## Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
mp = {}
for num in nums:
    if num in mp:
        print("Found it", num * mp[num])
        break
    mp[2020 - num] = num

## 3 numbers
## Sort and compare O(nlogn) + O(n^2) => O(n^2)
def getProduct(nums, num):
    nums.sort()
    i, n = 0, len(nums)
    while i < n:
        l, r = i + 1, n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == num:
                return nums[i] * nums[l] * nums[r]
            elif total < num:
                l += 1
            else:
                r -= 1
        i += 1

print("Found it", getProduct(nums, 2020))
