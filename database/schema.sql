-- Database: smart_hotel_ai
-- Table 1: hotel_demand_data
CREATE TABLE IF NOT EXISTS hotel_demand_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    base_price FLOAT,
    past_occupancy FLOAT,
    weather_score FLOAT,
    season INT,
    day_type INT,
    demand_percent FLOAT
);

-- Table 2: pricing_output
CREATE TABLE IF NOT EXISTS pricing_output (
    id INT AUTO_INCREMENT PRIMARY KEY,
    predicted_demand FLOAT,
    old_price FLOAT,
    new_price FLOAT,
    available_rooms INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Table 3 : daily_revenue
CREATE TABLE IF NOT EXISTS daily_revenue(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date Date,
    revenue_before DECIMAL(10,2),
    revenue_after DECIMAL(10,2),
    profit DECIMAL(10,2),
    booked_rooms INT
    );
