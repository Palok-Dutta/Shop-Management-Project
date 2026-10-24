def add_income(balance, amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return balance + amount


def add_expense(balance, amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if amount > balance:
        raise ValueError("Not enough balance")
    return balance - amount


def calculate_profit(income, expenses):
    return income - expenses


def can_afford(balance, amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return balance >= amount
