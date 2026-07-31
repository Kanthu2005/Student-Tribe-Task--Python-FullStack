def move_zeros_to_end(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1

arr = [0, 1, 0, 3, 12]
print("Original Array:", arr)
move_zeros_to_end(arr)
print("Array after moving zeros to the end:", arr)