
# 🧪 Key-Value Store Hands-On Lab: Product Inventory Lookup

## Overview

This lab introduces the Key-Value Data Model using Redis: We will install Redis via Docker, load product inventory data, and perform CRUD operations using Python.

---

## 🛠️ 1. Setup Instructions

### Prerequisites
- Docker installed
- Python 3.8+
- Visual Studio Code or any IDE
- Git

### Step 1: Clone the Lab Repository
```bash
git clone https://github.com/your-username/product-inventory-kv-lab.git
cd product-inventory-kv-lab
```

### Step 2: Start Redis with Docker
```bash
docker-compose up -d
```

Verify:
```bash
docker ps
```

---

## 💾 2. Load Sample Data

### Step 1: Install Python Dependencies
```bash
pip install redis
```

### Step 2: Run Import Script
```bash
cd scripts
python import_data.py
```

This loads `products.json` into Redis using `product_id` as keys.

---

## 🔁 3. Perform CRUD Operations

Use `interact_with_redis.py` to:
- Add new products
- Read product details
- Update values (e.g., price, stock)
- Delete entries

Example:
```bash
python interact_with_redis.py
```

---

## 🔍 4. Applied Scenario: Product Inventory Lookup

### Context:
E-commerce systems often require rapid lookup of product information by unique ID. A key-value store like Redis is ideal due to:
- Constant-time access
- Simplicity
- Scalability

### Example Use:
```redis
GET prod_1005
```

Expected Output:
```json
{
  "name": "Product 5",
  "category": "Books",
  "price_KES": 780.50,
  "in_stock": true,
  "quantity": 21,
  "rating": 4.2
}
```

---

## 🧪 5. Visuals and Output

Sample command line output:

```
✅ Successfully imported 20 products into Redis.
📦 Product Data: {'name': 'Product 6', 'price_KES': 299.99, 'in_stock': False, ...}
```

Screenshot suggestions:
- Redis CLI session
- Python script output

---

## 👥 6. Group Collaboration Summary

David Gathage, - Setup & Scripts
Stephen Okwiri - Docker & Markdown Guide
Alan Logedi - Data Generation & Testing
Sarah Mongare - Documentation & Reporting

---

## ✅ 7. Notes
- Redis version: `7.2`
- Python version: `3.10`
- Tested on: Ubuntu 22.04, Windows 11

---
