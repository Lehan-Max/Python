lst_1=[1,2,3,4]
lst_2=[4,5,6,7]
lst=[]
for i in range(len(lst_1)): # to iterate only till length of list instead of uneccesary iterations
     lst.append(lst_1[i]+lst_2[i]) # adding each individual ele of both list
print(lst)