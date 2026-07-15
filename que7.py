products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics", "quantity": 10},
    {"name": "Phone", "price": 800, "category": "Electronics", "quantity": 3},
    {"name": "Shoes", "price": 60, "category": "Fashion", "quantity": 15},
    {"name": "Watch", "price": 1500, "category": "Fashion", "quantity": 2},
    {"name": "Fridge", "price": 2000, "category": "Appliances", "quantity": 5},
    {"name": "Book", "price": 20, "category": "Stationery", "quantity": 0},
]

def low_stock(products, threshold=5):
    for product in products:
        if product["quantity"] < threshold:
            yield product
for item in low_stock(products):
    print(f"Low stock item: {item['name']} with quantity {item['quantity']}")

def expensive_items(products, min_price=1000):
    for product in products:
        if product["price"] > min_price:
            yield product
for item in expensive_items(products):
    print(f"Expensive item: {item['name']} priced at ${item['price']}") 

category = "Electronics"
uppercase_names = [product["name"].upper() for product in products if product["category"] == category]

products = list(map(lambda p: {**p, "price": p["price"] * 1.1}, products))

product_in_stock = list(filter(lambda p: p["quantity"] > 0, products))

import json

with open("inventory.json", "w") as f:
    json.dump(products, f, indent=4)

with open("inventory.json", "r") as f:
    data = f.read()
    print("Total character count in file:", len(data))