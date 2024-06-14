from lib.config import CONN, CURSOR

class Reviews:
    # Create review
    @classmethod
    def create_review(cls, user_id, book_id, review_text, rating):
        sql = """INSERT INTO Reviews (user_id, book_id, review, rating) VALUES (?, ?, ?, ?)"""
        CURSOR.execute(sql, (user_id, book_id, review_text, rating))
        CONN.commit()

    # Get review by ID
    @classmethod
    def get_review_by_id(cls, review_id):
        sql = "SELECT * FROM Reviews WHERE id = ?"
        CURSOR.execute(sql, (review_id,))
        return CURSOR.fetchone()

    # Update review
    @classmethod
    def update_review(cls, review_id, review_text, rating):
        sql = "UPDATE Reviews SET review = ?, rating = ? WHERE id = ?"
        CURSOR.execute(sql, (review_text, rating, review_id))
        CONN.commit()

    # Delete review
    @classmethod
    def delete_review(cls, review_id):
        sql = "DELETE FROM Reviews WHERE id = ?"
        CURSOR.execute(sql, (review_id,))
        CONN.commit()

    # Get reviews by user ID
    @classmethod
    def get_reviews_by_user_id(cls, user_id):
        sql = "SELECT * FROM Reviews WHERE user_id = ?"
        CURSOR.execute(sql, (user_id,))
        return CURSOR.fetchall()

# Example usage (optional)
if __name__ == "__main__":
    # Create a new review
    Reviews.create_review(user_id=1, book_id=1, review_text="Great book, loved the plot!", rating=5)

    # Get review by ID
    review = Reviews.get_review_by_id(1)
    print("Review by ID:", review)

    # Update review
    Reviews.update_review(1, "Updated review: Excellent read!", rating=4)

    # Get reviews by user ID
    user_reviews = Reviews.get_reviews_by_user_id(1)
    print("Reviews by User ID:")
    for review in user_reviews:
        print(review)

    # Delete review
    Reviews.delete_review(1)

    # Verify deletion by attempting to retrieve the deleted review
    deleted_review = Reviews.get_review_by_id(1)
    print("Deleted Review (should be None):", deleted_review)
