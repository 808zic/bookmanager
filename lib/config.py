import sqlite3

CONN = sqlite3.connect('blogs.db')
CURSOR = CONN.cursor()

class Database:
    def create_table(self):
        sql1 = """
        CREATE TABLE IF NOT EXISTS Users
          (id INTEGER PRIMARY KEY,
          name VARCHAR(55), 
          email VARCHAR(22), 
          age INTEGER)"""
        CURSOR.execute(sql1)

        sql2 = """
        CREATE TABLE IF NOT EXISTS Books
          (id INTEGER PRIMARY KEY,
          title VARCHAR(55),
          author VARCHAR(22), 
          genre VARCHAR(22),
          year INTEGER,
          user_id INTEGER,
          FOREIGN KEY (user_id) REFERENCES Users(id))
        """
        CURSOR.execute(sql2)

        sql3 = """
        CREATE TABLE IF NOT EXISTS Reviews
        (id INTEGER PRIMARY KEY,
        user_id INTEGER, 
        book_id INTEGER, 
        review VARCHAR(22), 
        rating INTEGER,
        FOREIGN KEY (book_id) REFERENCES Books(id),
        FOREIGN KEY (user_id) REFERENCES Users(id))
        """
        CURSOR.execute(sql3)
       
        CONN.commit()

    def drop_tables(self):
        sql = """ DROP TABLE IF EXISTS Users"""
        CURSOR.execute(sql)
        sql = """ DROP TABLE IF EXISTS Books"""
        CURSOR.execute(sql)
        sql = """ DROP TABLE IF EXISTS Reviews"""
        CURSOR.execute(sql)
    
        CONN.commit()

db = Database()
print("**********DROPPING Tables**********")
db.drop_tables()

print("**********CREATING Tables>>>>>>>>>>>>>>>>>>>")
db.create_table()

print("**********TABLES CREATED>>>>>>>>>>>>>>>>>>>")
