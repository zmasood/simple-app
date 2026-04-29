from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Secret is: {os.getenv('SECRET_KEY', 'Not Set')}"

if __name__ == "__main__":
    app.run(debug=False)
