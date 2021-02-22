# Given two arrays and value: a,b,d
# Return number of items in a where abs(ai - bi) > d
# O(n^2) possible, but can we do it faster?

# O(nlogn), sort and binary search
def getComparator(a, b, d):
    if d < 0:
        return len(a)
    
    m, n, res = len(a), len(b), 0

    a.sort()
    b.sort()

    for x in a:
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if abs(b[mid] - x) <= d:
                break
            if x > b[mid]:
                l = mid + 1
            else:
                r = mid - 1
        if l > r:
            res += 1
    return res

print(getComparator([7, 5, 9], [13, 1, 4], 3))

def getIndex(x, d):
    return x if d == 0 else x // d

def getComparatorOptimized(a, b, d):
    if d < 0:
        return len(a)
    
    m, n = len(a), len(b)
    mp = {}

    for i in range(n):
        x = b[i]
        index = getIndex(x, d)

        if index not in mp:
            mp[index] = (x, x)
        else:
            mp[index][0] = min(mp[index][0], x)
            mp[index][1] = max(mp[index][1], x)

    res = 0
    for i in range(m):
        x = a[i]
        index = getIndex(x, d) - 1

        found = False
        for j in range(n):
            if index not in mp:
                index += 1
                continue
            if abs(mp[index][0] - x) <= d:
                found = True
                break
            if abs(mp[index][1] - x) <= d:
                found = True
                break

            index += 1

        if not found:
            res += 1


    return res

print(getComparatorOptimized([7, 5, 9], [13, 1, 4], 3))