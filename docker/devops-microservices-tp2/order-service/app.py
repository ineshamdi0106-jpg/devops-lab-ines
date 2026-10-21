import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

PRODUCT_SERVICE_URL = os.environ.get("PRODUCT_SERVICE_URL", "http://product-service:5000")
orders = []

@app.route("/health")
def health():
    return jsonify({"service": "Order Service", "status": "running"})

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    try:
        resp = requests.get(f"{PRODUCT_SERVICE_URL}/products")
        if resp.status_code == 200:
            products = resp.json()
            product = next((p for p in products if p["id"] == product_id), None)
            
            if not product:
                return jsonify({"error": "Product not found"}), 404

            total = product["price"] * quantity
            order = {
                "order_id": len(orders) + 1,
                "product_name": product["name"],
                "quantity": quantity,
                "total": total
            }
            orders.append(order)
            return jsonify(order), 201
        else:
            return jsonify({"error": "Failed to reach product service"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
