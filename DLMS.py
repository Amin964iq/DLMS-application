# Define a class to represent a book with attributes: book_id, title, and author
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

# Define a function for the Quick Sort algorithm to sort a list of books based on book_id
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Choose the first book as the pivot
        pivot = arr[0].book_id
        # Separate books into two lists: less (<= pivot) and greater (> pivot)
        less = [book for book in arr[1:] if book.book_id <= pivot]
        greater = [book for book in arr[1:] if book.book_id > pivot]
        # Recursively apply Quick Sort to the less and greater lists and combine them
        return quick_sort(less) + [arr[0]] + quick_sort(greater)

# Define a function for the Binary Search algorithm to find a book by book_id in a sorted list
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # Check if the middle book has the desired book_id
        if arr[mid].book_id == key:
            return arr[mid]
        # If the desired book_id is less than the middle book's book_id, search in the left half
        elif arr[mid].book_id < key:
            low = mid + 1
        # If the desired book_id is greater than the middle book's book_id, search in the right half
        else:
            high = mid - 1
    # If the book is not found, return None
    return None

# Define a function to print book details
def print_books(books):
    for book in books:
        print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

# Sample data for the top 5 famous books
books_data = [
    Book(3, "To Kill a Mockingbird", "Harper Lee"),
    Book(1, "1984", "George Orwell"),
    Book(4, "The Great Gatsby", "F. Scott Fitzgerald"),
    Book(2, "The Catcher in the Rye", "J.D. Salinger"),
    Book(5, "Pride and Prejudice", "Jane Austen"),
]

# Sorting books using Quick Sort
sorted_books = quick_sort(books_data)

# Searching for a book by ID
searched_book = binary_search(sorted_books, 2)

# Printing sorted books
print("Sorted Books:")
print_books(sorted_books)

# Printing the searched book
if searched_book:
    print("\nSearched Book:")
    print(f"Book ID: {searched_book.book_id}, Title: {searched_book.title}, Author: {searched_book.author}")
else:
    print("\nBook not found.")
