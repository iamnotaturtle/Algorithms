# Heap implementation with underlying array
# https://towardsdatascience.com/data-structure-heap-23d4c78a6962
class Heap:
    def __init__(self, arr, isMax = False):
        self.isMax = isMax
        self.arr = arr
        self.build_max_heap() if isMax else self.build_min_heap()
    
    def build_min_heap(self):
        for i in reversed(range(len(self.arr) // 2)):
            self.min_heapify(i)

    def build_max_heap(self):
        for i in reversed(range(len(self.arr) // 2)):
            self.max_heapify(i)

    def min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        length = len(self.arr) - 1

        if left <= length and self.arr[i] > self.arr[left]:
            smallest = left
        if right <= length and self.arr[smallest] > self.arr[right]:
            smallest = right
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest) 

    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        length = len(self.arr) - 1

        if left <= length and self.arr[left] > self.arr[i]:
            largest = left
        if right <= length and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)

    def get_kth_largets(self, k):
        

hp = Heap([1,14, 2, 16, 3, 8, 4, 7, 9, 10])
print("min", hp.arr)

hp = Heap([1,14, 2, 16, 3, 8, 4, 7, 9, 10], True)
print("max", hp.arr)