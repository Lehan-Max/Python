def searchLinear(lst, ele):
    index = 0
    for i in lst:
        if i in lst:
            return index
        index += 1
    return -1


def bubbleSort(lst):
    for i in range (len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1]= lst[j+1], lst[j]
l =[3,4,5,6,2]
bubbleSort(l)
print(l)


ele = 66
res = searchLinear([1,2,3,4,2,6,7,8],ele)
if res == -1:
    print(f"{ele} is  found")
else:
    print(f"{ele} is not found")