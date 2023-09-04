# Определяем класс Book
class Book:
    def __init__(self, title, author):
        self.title = title # Атрибут: название книги
        self.author = author # Атрибут: автор книги
        self.checked_out = False # Атрибут: флаг, указывающий, взята ли книга

    def checkout(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"The book '{self.title}' is already checked out.")

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' is not checked out.")

# Определяем класс Library
class Library:
    def __init__(self):
        self.books = [] # Атрибут: список книг в библиотеке

    def add_book(self, book):
        self.books.append(book) # Метод: добавление книги в библиотеку

    def list_books(self):
        for book in self.books:
            print(f"'{book.title}' by {book.author}") # Метод: вывод списка книг

# Создаем экземпляры классов Book и Library
library = Library()
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Добавляем книги в библиотеку
library.add_book(book1)
library.add_book(book2)

# Выводим список книг в библиотеке
library.list_books()

# Берем книгу из библиотеки и возвращаем ее
book1.checkout()
book1.return_book()