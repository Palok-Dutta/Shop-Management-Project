import random


def calculate_price(price, demand):
    if price < 0:
        raise ValueError("Price cannot be negative")
    return round(price + price * demand / 100, 2)


def apply_discount(price, discount_percent):
    if price < 0 or not 0 <= discount_percent <= 100:
        raise ValueError("Invalid price or discount")
    return round(price * (1 - discount_percent / 100), 2)


def random_price_change(price, percentage):
    if price < 0 or not 0 <= percentage <= 100:
        raise ValueError("Invalid price or percentage")
    change = random.uniform(-percentage, percentage)
    return round(price * (1 + change / 100), 2)
