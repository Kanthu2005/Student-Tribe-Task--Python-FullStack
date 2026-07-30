#2.Find the largest element in an array
arr=[1, 2, 3, 4, 5]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print("Largest element is:",largest)