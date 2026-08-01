#Find union of two sorted arrays
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
def union_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    union_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union_arr.append(arr2[j])
            j += 1
        else:
            union_arr.append(arr1[i])
            i += 1
            j += 1
    while i < len(arr1):
        union_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        union_arr.append(arr2[j])
        j += 1
    return union_arr

print(union_sorted_arrays(arr1, arr2))