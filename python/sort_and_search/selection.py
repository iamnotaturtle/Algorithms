def selection(arr):
    i = 0
    n = len (arr)
    while i < n:
        small = i
        j = i + 1
        while j < n:
            small = j if arr[j] < arr[small] else small
            j += 1
        arr[i], arr[small] = arr[small], arr[i]
        i += 1
    return arr

assert(selection([7, 4, 3, 1, 8]) == [1, 3, 4, 7, 8])
