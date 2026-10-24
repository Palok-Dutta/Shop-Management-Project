def add_stock(inventory, name, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    result = [product.copy() for product in inventory]
    for product in result:
        if product["name"].lower() == name.lower():
            product["stock"] += quantity
            return result
    raise ValueError("Product not found")


def remove_stock(inventory, name, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    result = [product.copy() for product in inventory]
    for product in result:
        if product["name"].lower() == name.lower():
            if quantity > product["stock"]:
                raise ValueError("Not enough stock")
            product["stock"] -= quantity
            return result
    raise ValueError("Product not found")


def check_stock(inventory, name):
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product["stock"]
    return None


def low_stock(inventory, limit):
    return [product.copy() for product in inventory if product["stock"] <= limit]
