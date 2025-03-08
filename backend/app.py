from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up the PostgreSQL database URI (replace with your credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://youruser:yourpassword@localhost/yourdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define a User model (table)
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Float, nullable=True)  # Height in cm
    weight = db.Column(db.Float, nullable=True)  # Weight in kg
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'height': self.height,
            'weight': self.weight,
            'age': self.age
        }

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        height=data['height'],
        weight=data['weight'],
        age=data['age']
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(new_user.to_dict()), 201

# Endpoint to get user details by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify(user.to_dict())

# Endpoint to update user data
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    
    data = request.get_json()
    
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.height = data.get('height', user.height)
    user.weight = data.get('weight', user.weight)
    user.age = data.get('age', user.age)
    
    db.session.commit()
    
    return jsonify(user.to_dict())

# Endpoint to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted successfully'}), 200

# Start the app
if __name__ == '__main__':
    app.run(debug=True)
