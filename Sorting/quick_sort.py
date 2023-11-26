"""
Quick sort, also known as partition-exchange sort, is an in-place sorting algorithm. 
It is a divide-and-conquer algorithm that works on the idea of selecting a pivot element
and dividing the array into two subarrays around that pivot.
In quick sort, after selecting the pivot element, the array is split into two subarrays. 
One subarray contains elements smaller than the pivot element, 
and the other subarray contains elements greater than the pivot element.
"""


def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]

        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

        temp = arr[i + 1]
        arr[i + 1] = arr[high]
        arr[high] = temp

        return i + 1

    def quickSort(arr, low, high):
        if low < high:
            pivotIdx = partition(arr, low, high)
            quickSort(arr, low, pivotIdx - 1)
            quickSort(arr, pivotIdx + 1, high)

    quickSort(arr, 0, len(arr) - 1)

    return arr


assert quick_sort([5, 4, 10, 11, 1]) == [1, 4, 5, 10, 11]
assert quick_sort([10, 80, 30, 90, 40, 50, 70]) == [10, 30, 40, 50, 70, 80, 90]
