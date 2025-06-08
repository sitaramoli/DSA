# Selection Sort

arr = [4, 65, 32, 12, 0, -2, 6, 90, 3]

n = len(arr)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"Sorted Array: {arr}")
