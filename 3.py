def print_orders(orders):
    """
    Processes and prints customer orders from a list of tuples.
    
    Each tuple contains (customer_name, product, quantity).
    """
    for i, (customer_name, product, quantity) in enumerate(orders, start=1):
        print(f"Order {i}: {customer_name} ordered {quantity} {product}(s).")

# Sample order data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3),  # Additional orders for demonstration
]

# Call the function with the sample data
print_orders(orders)
