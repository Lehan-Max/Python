name = input("enter your name: ")
lst = ['a','e','i','o','u']
#using lambda
print(len(list(filter(lambda x:x in lst,name))))





#using for
c=0
for n in name:
    if n in lst:
        c+=1

print(c)
