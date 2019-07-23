def result(name, *args):

    res = 0
    for i in args:
        res += i
    print(f"Name: {name} Total: {res}")

res=result("Rajesh",67, 89, 56, 98, 45,67)
