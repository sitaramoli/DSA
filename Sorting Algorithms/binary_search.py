def binary_search(array, target_value):
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if array[mid_index] == target_value:
            return mid_index
        elif array[mid_index] < target_value:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 19
result = binary_search(arr, target)
if result != -1:
    print(f"{target} found at index: {result}")
else:
    print(f"{target} not found")
