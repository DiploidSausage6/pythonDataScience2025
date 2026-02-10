# This is a database management application that will involve viewing, adding, editing, and deleting the data. Note on YAML: You will need the pyyaml library installed for this to run. If you don't have it, you can install it via terminal using: pip install pyyaml.

import yaml
import os

books_initial = [
    {'title': 'The Outsiders', 'author': 'S.E. Hinton', 'page_count': 192},
    {'title': 'Holes', 'author': 'Louis Sachar', 'page_count': 233},
    {'title': 'The Giver', 'author': 'Lois Lowry', 'page_count': 240}
]

DB_FILE = 'database.yaml'

def load_books():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as file:
        return yaml.safe_load(file) or []

def save_books(books):
    with open(DB_FILE, 'w') as file:
        yaml.dump(books, file, sort_keys=False)

def view_books():
    books = load_books()
    if not books:
        print("The library is empty!")
        return
    for book in books:
        # Use .get() to prevent crashes if a key is missing
        print(f"Title: {book.get('title')}, Author: {book.get('author')}, Pages: {book.get('page_count')}")

def add_book():
    books = load_books()
    try:
        new_title = input("What is the title? ")
        new_author = input("What is the author? ")
        new_page_count = int(input("What is the page count? "))
        
        books.append({
            'title': new_title,
            'author': new_author,
            'page_count': new_page_count
        })
        save_books(books)
        print("Book added and saved!")
    except ValueError:
        print("Invalid input! Page count must be a number.")

def edit_book():
    books = load_books()
    view_books()
    wanted_title = input("\nTitle to edit: ")
    
    for book in books:
        if book['title'] == wanted_title:
            wanted_change = input("Change title, author, or page_count? ")
            if wanted_change in book:
                new_val = input(f"New {wanted_change}: ")
                book[wanted_change] = int(new_val) if wanted_change == 'page_count' else new_val
                save_books(books)
                print("Update saved!")
                return
    print("Book not found.")

def delete_book():
    books = load_books()
    unwanted = input("Exact title to delete: ")
    updated_books = [b for b in books if b['title'] != unwanted]
    
    if len(updated_books) < len(books):
        save_books(updated_books)
        print(f"Deleted '{unwanted}'!")
    else:
        print("Book not found.")

while True:
    print("\n--- Library Menu ---")
    print("[1] Add, [2] View, [3] Delete, [4] Edit, [5] Quit")
    choice = input("Enter choice: ")
    if choice == '1': add_book()
    elif choice == '2': view_books()
    elif choice == '3': delete_book()
    elif choice == '4': edit_book()
    elif choice == '5': break
    else: print("Invalid choice.")
