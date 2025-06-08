# Merge Sort

def merge_sort(array):
    if len(array) <= 1:
        return array

    # Step 1: Divide
    mid_index = len(array) // 2
    left_half = merge_sort(array[:mid_index])
    right_half = merge_sort(array[mid_index:])

    # Step 2: Merge
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [4, 65, 32, 12, 0, -2, 6, 90, 3]
print(f"Sorted Array: {merge_sort(arr)}")
