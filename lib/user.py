from lib.config import CONN, CURSOR

class Users:
    # Create user
    @classmethod
    def create_user(cls, username, email, age):
        sql = """INSERT INTO Users (name, email, age) VALUES (?, ?, ?)"""
        CURSOR.execute(sql, (username, email, age))
        CONN.commit()
    
    # Get user by ID
    @classmethod
    def get_user_by_id(cls, user_id):
        sql = "SELECT * FROM Users WHERE id = ?"
        CURSOR.execute(sql, (user_id,))
        return CURSOR.fetchone()
    
    # Update user email
    @classmethod
    def update_user_email(cls, user_id, new_email):
        sql = "UPDATE Users SET email = ? WHERE id = ?"
        CURSOR.execute(sql, (new_email, user_id))
        CONN.commit()
    
    # Delete user
    @classmethod
    def delete_user(cls, user_id):
        sql = "DELETE FROM Users WHERE id = ?"
        CURSOR.execute(sql, (user_id,))
        CONN.commit()
    
    # Get all users
    @classmethod
    def get_all_users(cls):
        sql = "SELECT * FROM Users"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    # Get users by age range
    @classmethod
    def get_users_by_age_range(cls, min_age, max_age):
        sql = "SELECT * FROM Users WHERE age BETWEEN ? AND ?"
        CURSOR.execute(sql, (min_age, max_age))
        return CURSOR.fetchall()

# Example usage
if __name__ == "__main__":
    user1 = Users()
    user1.create_user("ken", "ken@gmail.com", 20)

    # Get user by ID
    user = Users.get_user_by_id(1)
    print(user)

    # Update user email
    Users.update_user_email(1, "ken_new@gmail.com")

    # Get all users
    all_users = Users.get_all_users()
    print(all_users)

    # Get users by age range
    users_in_range = Users.get_users_by_age_range(18, 30)
    print(users_in_range)

    # Delete user
    Users.delete_user(1)
