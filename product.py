# Define a list of products
products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Smartphone", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2500},
    {"id": 4, "name": "Keyboard", "price": 1500},
    {"id": 5, "name": "Monitor", "price": 8000}
]

# Function to list products
def list_products(product_list):
    print("Product List:")
    for product in product_list:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ₹{product['price']}")

# Call the function
if __name__ == "__main__":
    list_products(products)