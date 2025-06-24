import os
import random
import time
from sqlalchemy import create_engine, text

# Use environment variable
db_url = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:postgres@localhost:5432/fast_food_db')
engine = create_engine(db_url)

products = ["French Fries", "Burger", "Nachos", "Soda", "Milkshake", "Burrito", "Hot Dog", "Salad"]
qty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

print(f"Connecting to: {db_url}")
print("Starting order generation...")

for num in range(1, 50):
    name = random.choice(products)
    price = random.choice(qty) * num
    quantity = random.choice(qty)
    
    with engine.connect() as conn:
        with conn.begin():
            conn.execute(text(
                "INSERT INTO orders (name, price, quantity) VALUES (:name, :price, :quantity)"
            ), {"name": name, "price": price, "quantity": quantity})
    
    print(f"Created order {num}: {name} - ${price} x {quantity}")
    time.sleep(2)