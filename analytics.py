def total_sales(transactions):
    return sum(transaction["total"] for transaction in transactions)


def average_sale(transactions):
    if not transactions:
        return 0
    return total_sales(transactions) / len(transactions)


def best_selling_product(transactions):
    if not transactions:
        return None

    quantities = {}
    for transaction in transactions:
        name = transaction["product"]
        quantities[name] = quantities.get(name, 0) + transaction["quantity"]
    return max(quantities, key=quantities.get)


def calculate_profit(income, expenses):
    return income - expenses
