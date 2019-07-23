import random as rn
nums = rn.randint(1,1000) 
for nums in range(100,500):   #list comprehension    
    if nums % 7==0: 
        print(nums)