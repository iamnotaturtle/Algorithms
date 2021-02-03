from collections import Counter

# Boyce Moore Majority Algorithm
# Used for finding majority element (voting, etc)
# majority element > n // 2
def majority(a):
    k = 1
    maj = a[0]
    for i in range(1, len(a)):
        # If we reached the end, set a new majority
        if k == 0:
            maj = a[i]
            k = 1
        elif a[i] == maj:
            k += 1
        else:
            k -= 1
    return maj

votes = [2, 2, 4, 4, 4, 4, 4, 0, 4, 4, 9, 9]
mp = Counter(votes)

majorityNum = max(mp, key = mp.get)
assert(mp[majorityNum] > len(votes) // 2)

assert(majority(votes) == majorityNum)
