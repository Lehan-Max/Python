try:
    num1 = int(input("enter the num1:"))
    num2 = int(input("enter the num 2: "))
    print(num1**num2)
    print(num1/num2)
except ZeroDivisionError:
    print(f"nuum2 can't be Zero....")
except ValueError:
    print(f"Please enter only numbers...")
except Exception as e:
    print(f"Something went wrong {e}")