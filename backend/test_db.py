import psycopg2
from dotenv import load_dotenv
import os


def test_postgres_connection():
    # Load environment variables from .env
    load_dotenv()
    
    USER = os.getenv("user")
    assert USER
    PASSWORD = os.getenv("password")
    assert PASSWORD
    HOST = os.getenv("host")
    assert HOST
    PORT = os.getenv("port")
    assert PORT
    DBNAME = os.getenv("dbname")
    assert DBNAME

    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Get current time
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    assert result

    # Close the cursor and connection
    cursor.close()
    connection.close()
