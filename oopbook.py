class book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def summary(self):
        print(f"{self.title} has {self.pages} pages.")

book_title = input("ENTER THE BOOK TITLE: ")
book_pages = int(input("ENTER THE NUMBER OF PAGES: "))

borrowed_book = book(book_title, book_pages)
borrowed_book.summary()

