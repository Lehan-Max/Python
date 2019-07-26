#program to calculate Factorial

num = int(input("enter a number: "))
fact = 1

while num > 0:
    
    fact = fact*num
    num=num-1
print(f"factorial is: {fact}")