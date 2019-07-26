#program to add 1 to each digits of num and if added 1 to 9 it pgives val 0


num = input("enter a number: ")

inc = 0
count = 1

while True:
    if num == 0:
        break
    temp  = (num%10)
    if temp == 9:
        temp = 0
    else:
        temp = temp+1
    inc+inc+(temp*count)
    count=count*10
    num=num//10
print(f"Answer: {inc}")
