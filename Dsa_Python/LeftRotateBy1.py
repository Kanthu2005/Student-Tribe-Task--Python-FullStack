#6 Left rotate array by 1
arr=[1, 2, 3, 4, 5]
first_element=arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=first_element
print("Array after left rotation by 1:",arr)   