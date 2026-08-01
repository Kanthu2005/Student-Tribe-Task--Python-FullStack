#12 Find missing number in [1..n]
def find_missing_number(arr):
    n = len(arr) + 1
    Actual_sum = n * (n + 1) // 2
    sum_of_arr = sum(arr)
    missing_number = Actual_sum - sum_of_arr
    return missing_number
arr = [1, 2, 4, 5, 6]

print(find_missing_number(arr))