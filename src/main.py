from flask import Flask, jsonify, request

app = Flask(__name__)

# Example functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/math', methods=['GET'])
def math_operations():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 1))
    return jsonify({
        "add": add(a, b),
        "subtract": subtract(a, b),
        "multiply": multiply(a, b),
        "divide": divide(a, b)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
