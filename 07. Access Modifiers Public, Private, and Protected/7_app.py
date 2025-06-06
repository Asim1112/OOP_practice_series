# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, _salary, ssn):
        self.name = name
        self._salary = _salary
        self.__ssn = ssn

    
    def get(self):
        return self.__ssn



obj1 = Employee(name="Asim", _salary=80000, ssn="123456789")



print("Public:", obj1.name)
print("Protected:", obj1._salary)

# print("Private", obj1.__ssn)        # Error! cannot access private variable directly





print("Private:", obj1.get())         # accessing private varibale through get method
