# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference 
# to an Employee object that exists independently of it.




class Department():
    def __init__(self, emp_obj):
        self.object = emp_obj

    def show_department(self):
        emp_name = self.object.show_info()
        print(f"This department has employee {emp_name}")




class Employee():
    def __init__(self, emp_name):
        self.name = emp_name

    def show_info(self):
        return self.name



e1 = Employee("Marcus")

d1 = Department(e1)
d1.show_department()

del d1

print(e1.show_info())



















