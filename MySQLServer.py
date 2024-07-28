import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root._123_"
        )
        
        my_cursor = connection.cursor()

        my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print("Error creating database:", err)
    finally:
        myocursor.close()
        connection.close()

if __name__ == "__main__":
    create_database()
