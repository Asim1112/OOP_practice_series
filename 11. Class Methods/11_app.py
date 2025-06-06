# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to 
# increase the count when a new book is added.


class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    

b1 = Book("Atomic Habits")
b2 = Book("The Exodus")
b3 = Book("Dinosaurs World")

print(b1.get_total_books())






