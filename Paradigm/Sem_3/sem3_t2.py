class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

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

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
           print(f"'{book.title}' by {book.author}")


library = Library()
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

library.list_books()
book1.checkout()
book1.return_book()