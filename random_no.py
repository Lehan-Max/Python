import random as rn
lst = []
for i in range(1,21): #1st 20 rand nos
    lst.append(rn.randint(1,50))  #append the first 20 random nos between range 1-50 and find max and min

res = [max(lst), min(lst)]
print(res)