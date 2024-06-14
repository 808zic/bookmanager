from lib.config import CONN, CURSOR

class Books:
    # Create book
    @classmethod
    def create_book(cls, title, author, genre, year, user_id):
        sql = """INSERT INTO Books (title, author, genre, year, user_id) VALUES (?, ?, ?, ?, ?)"""
        CURSOR.execute(sql, (title, author, genre, year, user_id))
        CONN.commit()

    # Get book by ID
    @classmethod
    def get_book_by_id(cls, book_id):
        sql = "SELECT * FROM Books WHERE id = ?"
        CURSOR.execute(sql, (book_id,))
        return CURSOR.fetchone()

    # Update book title
    @classmethod
    def update_book_title(cls, book_id, new_title):
        sql = "UPDATE Books SET title = ? WHERE id = ?"
        CURSOR.execute(sql, (new_title, book_id))
        CONN.commit()

    # Delete book
    @classmethod
    def delete_book(cls, book_id):
        sql = "DELETE FROM Books WHERE id = ?"
        CURSOR.execute(sql, (book_id,))
        CONN.commit()

    # Get books by user ID
    @classmethod
    def get_books_by_user_id(cls, user_id):
        sql = "SELECT * FROM Books WHERE user_id = ?"
        CURSOR.execute(sql, (user_id,))
        return CURSOR.fetchall()

# Example usage (optional)
if __name__ == "__main__":
    # Create a new book
    Books.create_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 1)

    # Get book by ID
    book = Books.get_book_by_id(1)
    print("Book by ID:", book)

    # Update book title
    Books.update_book_title(1, "The Great Gatsby: Revised Edition")

    # Get all books by user ID
    user_books = Books.get_books_by_user_id(1)
    print("Books by User ID:", user_books)

    # Delete book
    Books.delete_book(1)
