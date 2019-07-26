lb = int(input("enter lower boud: "))
ub = int(input("enter upper bound: "))

for n in range(lb,ub+1):
    if n % 9 == 0 and n% 5!= 0:
        print(n) 