# 14 Reverse an array in-place
arr = [1, 2, 3, 4, 5]

def reverse_array(arr):
    s=0
    e=len(arr)-1
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return arr
print(reverse_array(arr))