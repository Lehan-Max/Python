'''Write a program to print the Fibonacci series up to the number 34. 
(Example: 0, 1, 1, 2, 3, 5, 8, 13, … '''

nterms = 10

n1 = 0
n2 = 1
count = 0

print("Fibonacci sequence upto",nterms,":")
while count < nterms:
   print(n1,end='  ')
   num = n1 + n2
# update values
   n1 = n2
   n2 = num
   count += 1
