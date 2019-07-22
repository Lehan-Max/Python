'''accept no. from user and reverse it'''

num = int(input("enter a number"))
rev=0
temp = num

while num != 0:
    rev=rev * 10 + num % 10
    num//=10

print(f" Reverse of {temp} is {rev}")
