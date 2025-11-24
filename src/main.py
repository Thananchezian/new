from flask import Flask, request, jsonify

app = Flask(__name__)

# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Security headers for ZAP
@app.after_request
def set_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Permissions-Policy'] = 'geolocation=(), camera=()'
    return response

# Home route
@app.route("/")
def home():
    return "Calculator API is running!"

# Calculation route
@app.route("/calc")
def calc():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 1))
        op = request.args.get("op", "+")
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "*":
        result = multiply(a, b)
    elif op == "/":
        result = divide(a, b)
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

