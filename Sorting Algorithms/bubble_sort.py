# Bubble Sort

arr = [4, 65, 32, 12, 0, -2, 6, 90, 3]

n = len(arr)

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print(f"Sorted Array: {arr}")
