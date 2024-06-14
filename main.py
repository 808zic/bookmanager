from lib.user import Users
from lib.book import Books
from lib.review import Reviews

# Create a new user
User1 = Users()
User1.create_user("ken", "ken@gmail.com", 20)
print("User created:", User1)

# Get user by ID
user = Users.get_user_by_id(1)
print("\nUser by ID:", user)

# Update user email
Users.update_user_email(1, "ken_new@gmail.com")
print("\nUser email updated")

# Get all users
all_users = Users.get_all_users()
print("\nAll Users:")
for user in all_users:
    print(user)

# Get users by age range
users_in_range = Users.get_users_by_age_range(18, 30)
print("\nUsers in Age Range (18-30):")
for user in users_in_range:
    print(user)

# Delete user
Users.delete_user(1)
print("\nUser deleted")

# Verify deletion by attempting to retrieve the deleted user
deleted_user = Users.get_user_by_id(1)
print("\nDeleted User (should be None):", deleted_user)

# ------------------------------------------------------

# Now, let's integrate the Books class methods:

# Create a new book
Books.create_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 1)
print("\nBook created")

# Get book by ID
book = Books.get_book_by_id(1)
print("\nBook by ID:", book)

# Update book title
Books.update_book_title(1, "The Great Gatsby: Revised Edition")
print("\nBook title updated")

# Get all books by user ID
user_books = Books.get_books_by_user_id(1)
print("\nBooks by User ID:")
for book in user_books:
    print(book)

# Delete book
Books.delete_book(1)
print("\nBook deleted")

# Verify deletion by attempting to retrieve the deleted book
deleted_book = Books.get_book_by_id(1)
print("\nDeleted Book (should be None):", deleted_book)

# ------------------------------------------------------

# Now, let's integrate the Reviews class methods:

# Create a new review
Reviews.create_review(user_id=1, book_id=1, review_text="Great book, loved the plot!", rating=5)
print("\nReview created")

# Get review by ID
review = Reviews.get_review_by_id(1)
print("\nReview by ID:", review)

# Update review
Reviews.update_review(1, "Updated review: Excellent read!", rating=4)
print("\nReview updated")

# Get reviews by user ID
user_reviews = Reviews.get_reviews_by_user_id(1)
print("\nReviews by User ID:")
for review in user_reviews:
    print(review)

# Delete review
Reviews.delete_review(1)
print("\nReview deleted")

# Verify deletion by attempting to retrieve the deleted review
deleted_review = Reviews.get_review_by_id(1)
print("\nDeleted Review (should be None):", deleted_review)
