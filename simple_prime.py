num = int(input("enter a number"))
nums = [i for i in range(2, num//2+1) if num % i != 0]
print(nums)