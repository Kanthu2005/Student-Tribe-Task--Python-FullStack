#2. Find the second largest element in an array
arr=[1, 2, 3, 4, 5]
largest=arr[0]
second_largest=arr[0]
for num in arr:
    if num>largest:
        largest=num     
        second_largest=largest
    elif num>second_largest and num!=largest:
        second_largest=num
print("Second largest element is:",second_largest) 
        