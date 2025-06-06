# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a 
# message including the dog's name.


class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


    def bark(self):
        print(f"The {self.name} was shouting Woof! Woof! Woof!")


d1 = Dog("Tommy" , "Labrador")


print(d1.name)
print(d1.breed)

d1.bark()

