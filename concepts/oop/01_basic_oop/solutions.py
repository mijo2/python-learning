# Basic OOP Exercises Solutions

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

# Test
book = Book("1984", "George Orwell", 328)
print(book.info())  # 1984 by George Orwell, 328 pages
book.mark_as_read()
print(book.is_read)  # True