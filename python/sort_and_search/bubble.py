def bubble(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
    return arr


assert(bubble([7, 4, 3, 1, 8]) == [1, 3, 4, 7, 8])