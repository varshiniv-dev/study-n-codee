class book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN


class library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(
                f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}")


my_library = library()
book1 = book("Edge of darkness trilogy", "Leigh Rivers", "1234567890")
book2 = book("Twisted series", "Ana Huang", "0987654321")
book3 = book("Shatter me series", "Tahereh Mafi", "1122334455")
book4 = book("Campus games", "Stephanie Alves", "6677889900")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.display_books()
found_book = my_library.search_book("Edge of darkness trilogy")
if found_book:
    print(
        f"Found book: Title: {found_book.title}, Author: {found_book.author}, ISBN: {found_book.ISBN}")
else:
    print("Book not found.")
