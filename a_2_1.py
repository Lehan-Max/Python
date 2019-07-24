import random as rn

while True:
    first=rn.randint(1,10)
    second=rn.randint(1,10)
    third=rn.randint(1,10)
    fourth=rn.randint(1,10)
    
    if first + second + third + fourth == 12:
        if first>second:
            diff= first-second
        else:
            diff=second-first
        if third == diff and fourth == (first+third):
            num=(first*1000)+(second*100)+(third*10)+(fourth*1)
            break
print(num)