#program for calculating Simple Intrest

Principle = int(input("enter the amount: "))
Rate_of_intrest = float(input("enter Intrest: "))
Time = float(input("enter the time: "))
print(f"Principle: {Principle} | Rate of intrest: {Rate_of_intrest} | Time: {Time} ")
Simple_Intrest = (Principle*Rate_of_intrest*Time)/100

print(Simple_Intrest)