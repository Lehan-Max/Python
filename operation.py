def sum(a,b):
    return a+b

def prod(a,b):
    return a*b

def power(a, b):
    return a**b

def getSum(fun, nums):
    res = nums[0]
    for i in nums[1:]:
        res = fun(res, i)
    return res

res = getSum(sum,[1,2,3,4,5])
print(res)