from library.services.library_services import LibraryService
from library.services.auth_service import AuthService

def main():
    auth_service = AuthService()
    library_service = LibraryService()

    print("Welcome to Library Management System")

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if not auth_service.login(username, password):
        print("Invalid credentials")
        return

    print("Login successful!")

    while True:
        print("\n1. Add Book")
        print("2. Register User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show Books")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            library_service.add_book(book_id, title, author)

        elif choice == "2":
            user_id = input("User ID: ")
            name = input("Name: ")
            library_service.register_user(user_id, name)

        elif choice == "3":
            book_id = input("Book ID to issue: ")
            library_service.issue_book(book_id)

        elif choice == "4":
            book_id = input("Book ID to return: ")
            library_service.return_book(book_id)

        elif choice == "5":
            library_service.show_books()

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
