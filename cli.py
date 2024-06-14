import sys
from lib.user import Users
from lib.book import Books
from lib.review import Reviews

def display_menu():
    print("Welcome to the BookManager CLI! by @zic")
    print("Choose an option:")
    print("1. Manage Users")
    print("2. Manage Books")
    print("3. Manage Reviews")
    print("4. Exit")

def manage_users():
    while True:
        print("\nUser Management Menu:")
        print("1. Create User")
        print("2. Get User by ID")
        print("3. Update User Email")
        print("4. Get All Users")
        print("5. Get Users by Age Range")
        print("6. Delete User")
        print("7. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            Users.create_user(name, email, age)
            print("User created successfully!")
        elif choice == '2':
            user_id = int(input("Enter user ID: "))
            user = Users.get_user_by_id(user_id)
            print("User details:", user)
        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            new_email = input("Enter new email: ")
            Users.update_user_email(user_id, new_email)
            print("User email updated successfully!")
        elif choice == '4':
            all_users = Users.get_all_users()
            print("\nAll Users:")
            for user in all_users:
                print(user)
        elif choice == '5':
            age_min = int(input("Enter minimum age: "))
            age_max = int(input("Enter maximum age: "))
            users_in_range = Users.get_users_by_age_range(age_min, age_max)
            print(f"\nUsers between ages {age_min} and {age_max}:")
            for user in users_in_range:
                print(user)
        elif choice == '6':
            user_id = int(input("Enter user ID to delete: "))
            Users.delete_user(user_id)
            print("User deleted successfully!")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def manage_books():
    while True:
        print("\nBook Management Menu:")
        print("1. Create Book")
        print("2. Get Book by ID")
        print("3. Update Book Title")
        print("4. Get Books by User ID")
        print("5. Delete Book")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            year = int(input("Enter year: "))
            user_id = int(input("Enter user ID: "))
            Books.create_book(title, author, genre, year, user_id)
            print("Book created successfully!")
        elif choice == '2':
            book_id = int(input("Enter book ID: "))
            book = Books.get_book_by_id(book_id)
            print("Book details:", book)
        elif choice == '3':
            book_id = int(input("Enter book ID: "))
            new_title = input("Enter new title: ")
            Books.update_book_title(book_id, new_title)
            print("Book title updated successfully!")
        elif choice == '4':
            user_id = int(input("Enter user ID: "))
            user_books = Books.get_books_by_user_id(user_id)
            print(f"\nBooks by User ID {user_id}:")
            for book in user_books:
                print(book)
        elif choice == '5':
            book_id = int(input("Enter book ID to delete: "))
            Books.delete_book(book_id)
            print("Book deleted successfully!")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def manage_reviews():
    while True:
        print("\nReview Management Menu:")
        print("1. Create Review")
        print("2. Get Review by ID")
        print("3. Update Review")
        print("4. Get Reviews by User ID")
        print("5. Delete Review")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            review_text = input("Enter review text: ")
            rating = int(input("Enter rating (1-5): "))
            Reviews.create_review(user_id, book_id, review_text, rating)
            print("Review created successfully!")
        elif choice == '2':
            review_id = int(input("Enter review ID: "))
            review = Reviews.get_review_by_id(review_id)
            print("Review details:", review)
        elif choice == '3':
            review_id = int(input("Enter review ID: "))
            review_text = input("Enter updated review text: ")
            rating = int(input("Enter updated rating (1-5): "))
            Reviews.update_review(review_id, review_text, rating)
            print("Review updated successfully!")
        elif choice == '4':
            user_id = int(input("Enter user ID: "))
            user_reviews = Reviews.get_reviews_by_user_id(user_id)
            print(f"\nReviews by User ID {user_id}:")
            for review in user_reviews:
                print(review)
        elif choice == '5':
            review_id = int(input("Enter review ID to delete: "))
            Reviews.delete_review(review_id)
            print("Review deleted successfully!")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            manage_users()
        elif choice == '2':
            manage_books()
        elif choice == '3':
            manage_reviews()
        elif choice == '4':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
