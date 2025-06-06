# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and
# access both from outside the class.



class Car():
    brand = "Mitsubishi"

    def start(self):
        print("This is a car")


car = Car()

print(car.brand)
car.start()

