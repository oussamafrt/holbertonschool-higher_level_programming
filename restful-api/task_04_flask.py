#!/usr/bin/python3


from flask import Flask, jsonify, request
app = Flask(__name__)


users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


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
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def get_add_user():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error":"Username is required"}), 404
    else:
        username = data["username"]
        return jsonify({"Message": "User added", "user": data}), 200
    

if __name__ == "__main__":
    app.run()
