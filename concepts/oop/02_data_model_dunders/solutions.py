# Data Model and Dunder Methods Exercises Solutions

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

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

# Test
book1 = Book("1984", "George Orwell", 328)
book2 = Book("1984", "George Orwell", 328)
print(str(book1))  # 1984 by George Orwell
print(repr(book1))  # Book(title='1984', author='George Orwell', pages=328)
print(book1 == book2)  # True