import psycopg2
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from .env
load_dotenv()


def connect_supabase():
    # Fetch variables
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    # Connect to the database
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        print("Connection successful!")
        
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()
        
        # Example query
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        print("Current Time:", result)

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed.")

    except Exception as e:
        print(f"Failed to connect: {e}")


app = Flask(__name__)

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="ligma"
)

API_IDENTIFIER = "llama-3.2-1b-instruct"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = client.chat.completions.create(
            model=API_IDENTIFIER,
            messages=[{"role": "user", "content": user_message}]
        )

        return jsonify({'response': response.choices[0].message.content})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to connect to LLM", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)



# get models func
# chat api route that hits the v1/chat/completions enpoint in the correct format