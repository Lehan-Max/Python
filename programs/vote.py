def cast_vote(age):
    assert age >=18, f"Age shouldn't be < 18, it was: {age}"
    print("Thank You for voting......")

try:
    age = int(input("enter Age: "))
    cast_vote(age)

except AssertionError as a:
    print(a)
else:
    print(f"You have entered a valid age: {age}")
finally:
    print("End....")
