# Simulated database (list of dictionaries)
store_list = []

# Add a new product
def add_product(product_code, product_name, qty, per_price):
    product = {
        "product_code": product_code,
        "product_name": product_name,
        "quantity": int(qty),
        "price_per_item": float(per_price)
    }
    store_list.append(product)
    return product

# Get all products
def get_products():
    return store_list

# Edit a product
def edit_product(product_code):
    for product in store_list:
        if product["product_code"] == product_code:
            return product
    return None

# Update a product
def update_product(product_code, product_name, qty, per_price):
    for product in store_list:
        if product["product_code"] == product_code:
            product["product_name"] = product_name
            product["quantity"] = int(qty)
            product["price_per_item"] = float(per_price)
            return product
    return None

# Delete a product
def delete_product(product_code):
    global store_list
    store_list = [product for product in store_list if product["product_code"] != product_code]
    return store_list

# Reset form (clear simulated data)
def reset_store():
    global store_list
    store_list.clear()
    return store_list
