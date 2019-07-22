
'''Write a program to accept a number “n” from the user; then display the sum of the following series:
1 + 1/2 + 1/3 + ……. + 1/n'''
sum=0
n=int(input("enter a number"))
for i in range(1,n):
    sum=sum+(1/i)
print(round(sum,2))
