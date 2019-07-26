def biggest(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

num1 = int(input("enter a num1: "))
num2 = int(input("enter a num2: "))
num3 = int(input("enter a num3: "))
largest = biggest(num1,num2,num3)
print(f"largest among 3 numbers is: {largest}")