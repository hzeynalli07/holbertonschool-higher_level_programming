#!/usr/bin/python3
"""Flask ilə sadə RESTful API."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}


@app.route("/")
def home():
    """Kök URL üçün salamlaşma mesajı."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Bütün istifadəçi adlarının siyahısını qaytarır."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """API-nın vəziyyətini qaytarır."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Konkret istifadəçinin məlumatlarını qaytarır."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Yeni istifadəçi əlavə edir."""
    # JSON-un düzgünlüyünü yoxla
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    
    # İstifadəçi adı varmı?
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # İstifadəçi artıq mövcuddurmu?
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # İstifadəçini əlavə et
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
