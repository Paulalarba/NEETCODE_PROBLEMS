class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def summary(self):
        (print(f"{self.title} by {self.author} has {self.pages} pages. /n"))
    

def add_book():
    list_of_books = []
    for i in range(list_of_books):
        title = input(f"ENTER THE BOOK TITLE: {i + 1}:")
        author = input(f"ENTER THE AUTHOR NAME: {i + 1}")
        pages =  int(input(f"ENTER THE NUMBER OF PAGES:{i + 1} "))

        book = Book(title, author, pages)
        list_of_books.append(book)
        return list_of_books

my_books = add_book()
print(f"\n SUMMARY OF BOOKS!\n")

for p in my_books:
    print(p.summary(), end="")
