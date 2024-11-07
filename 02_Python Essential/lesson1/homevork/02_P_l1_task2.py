# Завдання 2
#
# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class Book:
    class BookFeedback:
        def __init__(self, text):
            self.text = text
        
        def __str__(self):
            return self.text

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.feedback_list = []
    
    def add_feedback(self, text):
        self.feedback_list.append(Book.BookFeedback(text))

    def __repr__(self):
        return f"Book({self.author}, {self.title}, {self.year}, {self.genre})"

    def __str__(self):
        feedbacks = [str(feedback) for feedback in self.feedback_list]
        return f"{self.title} by {self.author}, {self.year}, {self.genre}\n{feedbacks}"

book = Book("George Orwell", "1984", 1949, "Dystopian")
book.add_feedback("An amazing read!")
book.add_feedback("Thought-provoking and chilling.")
print(book)

