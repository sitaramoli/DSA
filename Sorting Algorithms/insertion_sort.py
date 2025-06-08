# Insertion Sort

arr = [4, 65, 32, 12, 0, -2, 6, 90, 3]
n = len(arr)

for i in range(1, n):
    insert_index = i
    current_value = arr[i]
    for j in range(i - 1, -1, -1):
        if arr[j] > current_value:
            arr[j + 1] = arr[j]
            insert_index = j
    arr[insert_index] = current_value

print(f"Sorted Array: {arr}")
