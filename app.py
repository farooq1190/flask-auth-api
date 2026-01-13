from flask import Flask, jsonify
from dotenv import load_dotenv
import flask
from config import SECRET_KEY
from auth import auth_bp

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretkey"

app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return jsonify({
        "status": "API is running",
        "message": "Welcome to the Flask Authentication API"
    })

if __name__ == '__main__':
    app.run(debug=True)
