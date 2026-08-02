# 16  Prefix sum array construction
arr = [1, 2, 3, 4, 5]
def prefix_sum_array(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum
print(prefix_sum_array(arr))