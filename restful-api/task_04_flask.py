#!/usr/bin/python3


from flask import Flask, jsonify, request
app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_user():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user_by_username(username):
    user = users.get(username)
    if user:
        return jsonify(user), 201
    else:
        return jsonify({"error": "User not found"}), 400


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username in data:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
