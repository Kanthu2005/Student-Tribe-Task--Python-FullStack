#Python program for a smart parking system using "if", "elif", and "else" statements.
#week 1
h=int(input("Enter the hours: "))
if h<1:
    print("Invalid Input")
elif h>24:
    print("Invalid Parking Duration")
elif h>=1 and h<=2:
    amount=100
    print("Parking Amount is:",amount)  
elif h<=5:
    amount=100+(h-2)*40
    print("Parking Amount is:",amount)
elif h<=12:
    amount =100+(h-2)*40+(h-5)*30
    print("Parking Amount is:",amount)
elif h<=24:
    amount=500
    print("Parking Amount is:",amount)
  