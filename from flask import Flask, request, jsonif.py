from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data
users = {
    1: {"name": "John Doe", "email": "john@example.com"},
    2: {"name": "Jane Smith", "email": "jane@example.com"}
}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# POST - Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    user_id = max(users.keys()) + 1 if users else 1
    users[user_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"id": user_id, "message": "User added successfully"}), 201

# PUT - Update existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    users[user_id].update({
        "name": data.get("name", users[user_id]["name"]),
        "email": data.get("email", users[user_id]["email"])
    })
    return jsonify({"message": "User updated successfully"})

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
