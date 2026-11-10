from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 25}
]

@app.route("/")
def home():
    return jsonify({"service": "Product Service", "status": "running"})

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/health")
def health():
    return jsonify({"service": "Product Service", "status": "running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
