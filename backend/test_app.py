from dotenv import load_dotenv
import os


def test_environment_vars():
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
