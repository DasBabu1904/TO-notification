import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from time import sleep
import random
from models import Order
from meta import Base

# Use environment variable or default to localhost
db_url = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:postgres@localhost:5432/fast_food_db')
engine = create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()
products = [
    "French Fries",
    "Hamburguer", 
    "Nachos",
    "Soda",
    "Milkshake",
    "Burrito",
    "Hot Dog",
    "Salad",
]
qty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

print(f"Connecting to: {db_url}")
print("Starting order generation...")

for num in range(1, 200):
    order = Order(
        name=random.choice(products),
        price=random.choice(qty) * num,
        quantity=random.choice(qty)
    )
    db.add(order)
    db.commit()
    print(f"Created order {num}: {order.name} - ${order.price} x {order.quantity}")
    sleep(5)