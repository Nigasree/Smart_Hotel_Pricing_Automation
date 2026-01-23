import pandas as pd
import random
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# DATABASE Connection

engine = create_engine(
    "mysql+mysqlconnector://root:@localhost/smart_hotel_ai"
)

query = """
SELECT base_price, past_occupancy, weather_score, season, day_type, demand_percent
FROM hotel_demand_data
"""
df = pd.read_sql(query, engine)


# Training Data
X = df.drop("demand_percent", axis=1)
y = df["demand_percent"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


base_price = 3000
past_occupancy = random.randint(30, 95)
weather_score = round(random.uniform(0.2, 0.9), 2)
season = random.randint(1, 4)
day_type = random.randint(0, 1)

simulated_input = [[
    base_price,
    past_occupancy,
    weather_score,
    season,
    day_type
]]

prediction = model.predict(simulated_input)[0]
new_price = int(base_price * (1 + prediction / 100))
MIN_PRICE = 2500
MAX_PRICE = 6020
new_price = max(MIN_PRICE, min(new_price, MAX_PRICE))
total_rooms = 30
booked_rooms = int(total_rooms * (prediction / 100))
available_rooms = total_rooms - booked_rooms


# OUTPUT
print(" Smart Hotel Pricing Engine ")
print("Past Occupancy (%):", past_occupancy)
print("Weather Score:", weather_score)
print("Season:", season)
print("Day Type (0=Weekday, 1=Weekend):", day_type)
print("Predicted Demand (%):", round(prediction, 2))
print("Old Price:", base_price)
print("New Price (Auto Updated):", new_price)
print("Total Rooms:", total_rooms)
print("Available Rooms (Auto):", available_rooms)


output_df = pd.DataFrame([{
    "predicted_demand": round(prediction, 2),
    "new_price": new_price,
    "available_rooms": available_rooms
}])
output_df.to_sql("pricing_output", engine, if_exists="append", index=False)
