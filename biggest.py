def armstrong_num(num):
    num_1 = num
    res=0
    while num != 0:
        rem = num % 10
        res = res + rem ** 3
        num = num // 10
    return  num_1 == res

input_num = int(input("enter a number"))
if(armstrong_num(input_num)):
    print(f"given num {input_num} is armstrong")
else:
    print(f"given num {input_num} is not armstrong")