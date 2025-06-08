# Quick Sort

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    left = []
    right = []

    for i in array[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


def inplace_quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot_index = partition(array, low, high)
        inplace_quicksort(array, low, pivot_index - 1)
        inplace_quicksort(array, pivot_index + 1, high)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


arr = [4, 65, 32, 12, 0, -2, 6, 90, 3]

print(f"Quick Sorted Array: {quick_sort(arr)}")

inplace_quicksort(arr)
print(f"Inplace Sorted Array: {arr}")
