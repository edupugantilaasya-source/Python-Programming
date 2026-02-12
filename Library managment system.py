# ----------- Book Class -----------

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


# ----------- Library Class -----------

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book added successfully!\n")

    def view_books(self):
        if len(self.books) == 0:
            print("No books available.\n")
            return

        for book in self.books:
            status = "Available" if book.available else "Issued"
            print("ID:", book.book_id,
                  "| Title:", book.title,
                  "| Author:", book.author,
                  "| Status:", status)
        print()

    # ----------- SEARCH OPTION -----------

    def search_book(self):
        search_title = input("Enter Book Title to Search: ")

        found = False
        for book in self.books:
            if search_title.lower() in book.title.lower():
                status = "Available" if book.available else "Issued"
                print("Book Found:")
                print("ID:", book.book_id,
                      "| Title:", book.title,
                      "| Author:", book.author,
                      "| Status:", status)
                print()
                found = True

        if not found:
            print("Book not found!\n")

    def issue_book(self):
        book_id = input("Enter Book ID to Issue: ")

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully!\n")
                else:
                    print("Book already issued!\n")
                return

        print("Book not found!\n")

    def return_book(self):
        book_id = input("Enter Book ID to Return: ")

        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully!\n")
                else:
                    print("Book was not issued!\n")
                return

        print("Book not found!\n")


# ----------- Admin Login -----------

def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    if username == "admin" and password == "1234":
        print("\nLogin Successful!\n")
        return True
    else:
        print("\nInvalid Login!\n")
        return False


# ----------- Main Program -----------

def main():
    if not admin_login():
        return

    library = Library()

    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.issue_book()
        elif choice == "5":
            library.return_book()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
