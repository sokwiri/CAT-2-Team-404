import redis
import json

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

def create_product(product_id, product_data):
    if r.exists(product_id):
        print("❌ Product already exists.")
    else:
        r.set(product_id, json.dumps(product_data))
        print("✅ Product created.")

def read_product(product_id):
    data = r.get(product_id)
    if data:
        print("📦 Product Data:", json.loads(data))
    else:
        print("❌ Product not found.")

def update_product(product_id, field, new_value):
    data = r.get(product_id)
    if data:
        product = json.loads(data)
        product[field] = new_value
        r.set(product_id, json.dumps(product))
        print("🔄 Product updated.")
    else:
        print("❌ Product not found.")

def delete_product(product_id):
    if r.delete(product_id):
        print("🗑️ Product deleted.")
    else:
        print("❌ Product not found.")

def read_all_products():
    keys = r.keys("prod_*")
    if not keys:
        print("❌ No products found.")
        return
    print("📦 All Products:")
    for key in keys:
        data = r.get(key)
        if data:
            print(f"{key.decode()}: {json.loads(data)}")
# Example operations:
create_product("prod_1021", {
    "name": "New Product",
    "category": "Accessories",
    "price_KES": 1299,
    "in_stock": True,
    "quantity": 12,
    "rating": 4.3
})

read_product("prod_1021")
update_product("prod_1021", "price_KES", 1499)
delete_product("prod_1021")
read_all_products()
