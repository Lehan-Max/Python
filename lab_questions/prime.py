#program to calculate upper bound and lower bound given upper and lower bound

lower = int(input("enter a lower bound: "))
upper = int(input("enter a upper bound: "))

print(f"prime no. begins from {lower} and {upper} are: ", end='')

for i in range(lower, upper+1):
    flag = 0
    for j in range(2,(i//2+1)):
        if i%j == 0:
            flag = 1
    if flag == 0:
        print(f"{i }", end=' ')
        