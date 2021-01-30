# Work backwards!
def insertion(arr):
    i = 1
    n = len(arr)

    while i < n:
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
        i += 1
    return arr

assert(insertion([7, 4, 3, 1, 8]) == [1, 3, 4, 7, 8])
