from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash   
from models import get_user_by_username, create_user
from utils import generate_token,  verify_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "missing data"}), 400
    
    if get_user_by_username(data["username"]):
        return jsonify({"error": "user already exists"}), 409
    
    password_hash= generate_password_hash(data["password"])
    create_user(data["username"], password_hash)

    return jsonify({"message": "user created successfully"}), 201

@auth_bp.route("/test-register")
def test_register():
    from models import create_user

    create_user("testuser", generate_password_hash("1234"))
    return {"message": "Test user created"}


@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "missing data"}),400
    
    user = get_user_by_username(data["username"])

    if not user or not check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "invalid credentials"}), 401
    
    token = generate_token(user["username"])
    return jsonify({"token": token}), 200

@auth_bp.route("/api/profile", methods=["GET"])
def profile():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "missing token"}), 401
    
    token = auth_header.split(" ")[1]
    payload = verify_token(token)
    
    if not payload:
        return jsonify({"error": "invalid or expired token"}), 401
    
    user = get_user_by_username(payload["username"])
    if not user:
        return jsonify({"error": "user not found"}), 404
    
    return jsonify({
        "username": user["username"]
        }), 200

@auth_bp.route("/test-login")
def test_login():
    from models import get_user_by_username
    from utils import generate_token

    user = get_user_by_username("testuser")
    if not user:
        return {"error": "User not found"}

    token = generate_token("testuser")
    return {"token": token}

