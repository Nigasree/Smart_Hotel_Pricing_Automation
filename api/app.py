from flask import Flask, jsonify
import pandas as pd
import random
from sqlalchemy import create_engine

app = Flask(__name__)

# DB connection
engine = create_engine(
    "mysql+mysqlconnector://root:@localhost/smart_hotel_ai"
)

TOTAL_ROOMS = 30
BASE_PRICE = 2500

@app.route("/run-pricing", methods=["GET"])
def run_pricing():

    # ---- Simulated ML Output (replace later with real model) ----
    predicted_demand = round(random.uniform(40, 95), 2)

    # ---- Pricing Logic ----
    new_price = int(BASE_PRICE * (1 + predicted_demand / 100))
    MIN_PRICE = 2230
    MAX_PRICE = 6020
    new_price = max(MIN_PRICE, min(new_price, MAX_PRICE))

    # ---- Availability ----
    booked_rooms = int(TOTAL_ROOMS * (predicted_demand / 100))
    available_rooms = TOTAL_ROOMS - booked_rooms

    # ---- Revenue & Profit (DAILY) ----
    revenue_before = BASE_PRICE * booked_rooms
    revenue_after = new_price * booked_rooms
    profit = revenue_after - revenue_before

    return jsonify({
        "status": "success",
        "predicted_demand": predicted_demand,
        "old_price": BASE_PRICE,
        "new_price": new_price,
        "booked_rooms": booked_rooms,
        "available_rooms": available_rooms,
        "revenue_before": revenue_before,
        "revenue_after": revenue_after,
        "profit": profit
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
