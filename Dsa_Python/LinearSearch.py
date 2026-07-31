#9 Linear search in array
a=[5, 3, 8, 6, 2]
x=8
for i in range(len(a)):
    if a[i]==x:
        print("Element found at index", i)
        break
else:
    print("Element not found")