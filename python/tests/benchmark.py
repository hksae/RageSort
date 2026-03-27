import time
import random
import sys
from ragesort import bit_radix_sort

sys.setrecursionlimit(2000000)

def quicksort(arr):
    def _quicksort(items, low, high):
        if low < high:
            split_index = _partition(items, low, high)
            _quicksort(items, low, split_index)
            _quicksort(items, split_index + 1, high)

    def _partition(items, low, high):
        pivot = items[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while items[i] < pivot:
                i += 1
            j -= 1
            while items[j] > pivot:
                j -= 1
            if i >= j:
                return j
            items[i], items[j] = items[j], items[i]

    copy_arr = arr[:]
    _quicksort(copy_arr, 0, len(copy_arr) - 1)
    return copy_arr

sizes = [1000, 10000, 100000, 500000]
print(f"{'Size':<10} | {'RageSort (ms)':<15} | {'QuickSort (ms)':<15} | {'Ratio'}")
print("-" * 55)

for size in sizes:
    data = [random.randint(-10 ** 6, 10 ** 6) for _ in range(size)]

    t0 = time.perf_counter()
    bit_radix_sort(data)
    t1 = time.perf_counter()
    rage_time = (t1 - t0) * 1000

    t0 = time.perf_counter()
    quicksort(data)
    t1 = time.perf_counter()
    quick_time = (t1 - t0) * 1000

    ratio = quick_time / rage_time
    print(f"{size:<10} | {rage_time:<15.2f} | {quick_time:<15.2f} | {ratio:.2f}x")
