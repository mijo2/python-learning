# Data Model and Dunder Methods Exercises

# Exercise: Data Model and Dunder Methods
# Assume you have a Book class from basic_oop.
# Extend it with:
# - __str__ method for user-friendly representation
# - __repr__ method for developer representation
# - __eq__ method to compare books by title and author
# - __hash__ method for hashing (use title and author)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False

    def info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def mark_as_read(self):
        self.is_read = True

# TODO: Add dunder methods to Book class

# Test
# book1 = Book("1984", "George Orwell", 328)
# book2 = Book("1984", "George Orwell", 328)
# print(str(book1))  # e.g., "1984 by George Orwell"
# print(repr(book1)) # e.g., Book(title='1984', author='George Orwell', pages=328)
# print(book1 == book2)  # True