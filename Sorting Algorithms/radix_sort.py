# Radix Sort with Counting Sort

def counting_sort_digit(array, exp):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    for num in array:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in reversed(range(n)):
        index = (array[i] // exp) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1

    array[:n] = output[:n]


def radix_sort(array):
    if not array:
        return array

    max_value = max(array)
    exp = 1

    while max_value // exp > 0:
        counting_sort_digit(array, exp)
        exp *= 10

    return array


arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Sorted Array: {radix_sort(arr)}")
