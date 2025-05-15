
class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def display(self):
        return self.name, self.marks

student_details = Student(name="Alexander" , marks="772")
result = student_details.display()
print(result)