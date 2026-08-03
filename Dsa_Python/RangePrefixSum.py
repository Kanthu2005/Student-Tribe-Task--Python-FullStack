#17 Range sum query (immutable)
def kadanes(arr):
    max_sum=float('-inf')
    for i in range(len(arr)):
        current_sum=0
        for j in range(i,len(arr)):
            current_sum+=arr[j]
            max_sum=max(max_sum,current_sum)
    return max_sum
kadane_arr=[-2,1,-3,4,-1,2,1,-5,4]
print("maximum subarray sum:", kadanes(kadane_arr))