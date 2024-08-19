# Initial library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, new_book):
    # Check if the new book is already in the library
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} already exists in the library.")
    else:
        # Add the new book to the library
        library.append(new_book)
        print(f"Added '{new_book[0]}' by {new_book[1]} to the library.")

def display_library(library):
    print("Current Library Collection:")
    for book in library:
        print(f"Title: {book[0]}, Author: {book[1]}")

# Example usage
new_books = [
    ("To Kill a Mockingbird", "Harper Lee"),
    ("1984", "George Orwell"),  # Duplicate book
    ("The Great Gatsby", "F. Scott Fitzgerald")
]

for book in new_books:
    add_book(library, book)

display_library(library)
