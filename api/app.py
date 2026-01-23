from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/run-pricing", methods=["GET"])
def run_pricing():

    predicted_demand = round(random.uniform(40, 95), 2)
    base_price = 3000
    new_price = int(base_price * (1 + predicted_demand / 100))
    total_rooms = 30
    available_rooms = int(total_rooms * (predicted_demand / 100))

    return jsonify({
        "status": "success",
        "predicted_demand": predicted_demand,
        "old_price": base_price,
        "new_price": new_price,
        "available_rooms": available_rooms
    })

if __name__ == "__main__":
    app.run(port=5000)
