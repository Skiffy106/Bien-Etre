
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from openai import OpenAI
from supabase import create_client
import os
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="ligma"
)

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

API_IDENTIFIER = "llama-3.2-1b-instruct"
PRE_PROMPT_MESSAGE = "Respond only in riddles."

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    response = supabase.auth.sign_up({"email": email, "password": password})
    
    return jsonify(response.model_dump()), 201

@app.route("/signin", methods=["POST"])
def signin():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
    
    return jsonify(response.model_dump()), 200

from flask import request

def get_current_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    
    token = auth_header.split("Bearer ")[-1]
    user = supabase.auth.get_user(token)
    
    return user



@app.route('/chat', methods=['POST'])
def chat():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = client.chat.completions.create(
            model=API_IDENTIFIER,
            messages=[
                {"role": "system", "content": PRE_PROMPT_MESSAGE},
                {"role": "user", "content": user_message}
            ]
        )

        return jsonify({'response': response.choices[0].message.content})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to connect to LLM", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)

# get models func
# chat api route that hits the v1/chat/completions enpoint in the correct format


# Google OAuth with Supabase 
@app.route("/auth/google", methods=["GET"])
def google_auth():
    response = supabase.auth.sign_in_with_oauth(
            {"provider": "google", "redirect_to": "http://127.0.0.1:5000/auth/callback"}
        )
   
    return jsonify(response.model_dump()), 200  

      


 
