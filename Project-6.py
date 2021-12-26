# Python3 Program to
# input three number and find the greatest number.

# storing the numbers in the the variables - 'num1' , 'num2' , 'num3'
num1 = float(input("Enter the 1st number = "))
num2 = float(input("Enter the 2nd number = "))
num3 = float(input("Enter the 3rd number = "))
# adding if-elif-else statements to find the greatest number among the three numbers.
if num1 > num2 and num1 > num3:
    print("The largest number is", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is", num2)
elif num1 == num2 and num2 == num3:
    print("all are equal")
else:
    print("The largest number is", num3)
