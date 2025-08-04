import redis
import json

# Load the product data
with open("../sample_data/products.json", "r") as f:
    products = json.load(f)

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Insert products into Redis
for product_id, product_data in products.items():
    r.set(product_id, json.dumps(product_data))

print(f"✅ Successfully imported {len(products)} products into Redis.")
