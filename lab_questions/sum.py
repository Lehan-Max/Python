num = int(input("enter a number: "))
sum = 0
while True:
    if sum>1 and sum<=9:
        break

    sum = 0
    while True:
        if(num==0):
            break
        sum=sum+(num%10)
        num=num//10
    num=sum
print(f"sum is: {sum}")

#other method 

Tnum = num = int(input("enter a num"))

while num>9:
    sum = (num % 10 + num // 10)
    num = sum
print(f"The sum of digits of {Tnum} is {num}")