
#wrong


str1 = input("enter sring 1: ")
str2 = input("enter sring 2: ")
str3 = input("enter sring 3: ")

if str1.startswith("Does" or "Do" or "are") and str1.endswith("?"):
    print(f"{str1}: is interogative")
else: 
    print(f"{str1}: is sensitive")

if str2.startswith("Does" or "do" or "are") and str2.endswith('?'):
    print(f"{str2}: is interogative")
else: 
    print(f"{str2}: is sensitive")

if str3.startswith("Does" or "do" or "are") and str3.endswith('?'):
    print(f"{str3}: is interogative")
else:
    print(f"{str3}: is sensitive")
