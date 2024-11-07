# Завдання 1
#
# Створіть клас, який описує книгу.
# Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"Book({self.author}, {self.title}, {self.year}, {self.genre})"

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}, {self.genre}"

book1 = Book("J.K. Rowling", "Harry Potter and the Philosopher's Stone", 1997, "Fantasy")
book2 = Book("J.K. Rowling", "Harry Potter and the Chamber of Secrets", 1998, "Fantasy")

print(book1)
print(book2)