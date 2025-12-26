# Library Class 
# ● Create a class Library that stores a list of book titles. 
# ● Add methods add_book() and show_books(). 
# ● Test by adding a few books and displaying them.
class library:
    def __init__(self):
        self.books = []       
    def add_book(self,booktitle):
        self.books.append(booktitle)     
    def show_books(self): 
        for book in self.books:
            print(book)
lib =library()
lib.add_book("The Great Gatsby") 
lib.show_books()      

