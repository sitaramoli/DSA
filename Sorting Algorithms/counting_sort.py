def counting_sort(array):
    max_value = max(array)
    count_array = [0] * (max_value + 1)
    sorted_array = [0] * len(array)

    for num in array:
        count_array[num] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for num in array[::-1]:
        sorted_array[count_array[num] - 1] = num
        count_array[num] -= 1

    return sorted_array


arr = [170, 45, 75, 90, 802, 24, 2, 66]

print(f"Sorted Array: {counting_sort(arr)}")
