# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this
# exception if age < 18. Handle it with try...except.



class InvalidAgeError(Exception):
    pass

def check_age(age):
    eighteen = 18


    if age < eighteen:
        raise InvalidAgeError(f"Age must be {eighteen} or older.")
    else:
        print("Access granted!")



try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Access denied:", e)

except ValueError:
    print("Please enter a valid numeric age")

        

