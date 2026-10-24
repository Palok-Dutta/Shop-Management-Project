import json

import analytics
import finance
import inventory
import pricing
import searching
import sorting


def show_products(products):
    for product in products:
        print(
            product["name"],
            "| BDT", product["price"],
            "| stock:", product["stock"],
            "|", product["category"],
        )


def main():
    with open("products.json", encoding="utf-8") as file:
        products = json.load(file)

    balance = 0
    transactions = []

    while True:
        print("\n1 Search  2 Sort  3 Stock  4 Finance  5 Reports  6 Price  7 Sell  0 Exit")
        choice = input("Choose: ")

        try:
            if choice == "0":
                break

            elif choice == "1":
                name = input("Product name: ").lower()
                matches = [p for p in products if name in p["name"].lower()]
                show_products(matches)

            elif choice == "2":
                key = input("Sort by name or price: ").lower()
                if key not in ("name", "price"):
                    print("Choose name or price")
                    continue
                method = input("1 Bubble sort, 2 Selection sort: ")
                result = sorting.bubble_sort(products, key) if method == "1" else sorting.selection_sort(products, key)
                show_products(result)

            elif choice == "3":
                action = input("add, remove, check, or low: ").lower()
                if action == "low":
                    show_products(inventory.low_stock(products, int(input("Stock limit: "))))
                    continue
                name = input("Product name: ")
                if action == "check":
                    print("Stock:", inventory.check_stock(products, name))
                elif action == "add":
                    products = inventory.add_stock(products, name, int(input("Quantity: ")))
                elif action == "remove":
                    products = inventory.remove_stock(products, name, int(input("Quantity: ")))
                else:
                    print("Unknown stock action")

            elif choice == "4":
                action = input("income, expense, or balance: ").lower()
                if action == "income":
                    balance = finance.add_income(balance, float(input("Amount: ")))
                elif action == "expense":
                    balance = finance.add_expense(balance, float(input("Amount: ")))
                print("Balance: BDT", balance)

            elif choice == "5":
                print("Total sales:", analytics.total_sales(transactions))
                print("Average sale:", analytics.average_sale(transactions))
                print("Best selling:", analytics.best_selling_product(transactions))
                print("Profit:", analytics.calculate_profit(analytics.total_sales(transactions), 0))

            elif choice == "6":
                name = input("Product name: ").lower()
                product = searching.linear_search(
                    [{"name_key": p["name"].lower(), **p} for p in products],
                    name,
                    "name_key",
                )
                if product is None:
                    print("Product not found")
                    continue
                percent = float(input("Percentage: "))
                action = input("demand, discount, or random: ").lower()
                if action == "demand":
                    price = pricing.calculate_price(product["price"], percent)
                elif action == "discount":
                    price = pricing.apply_discount(product["price"], percent)
                else:
                    price = pricing.random_price_change(product["price"], percent)
                print("New price: BDT", price, "| Original price:", product["price"])

            elif choice == "7":
                name = input("Product name: ")
                quantity = int(input("Quantity: "))
                product = searching.linear_search(products, name, "name")
                if product is None:
                    print("Product not found")
                    continue
                total = product["price"] * quantity
                products = inventory.remove_stock(products, name, quantity)
                balance = finance.add_income(balance, total)
                transactions.append(
                    {"product": product["name"], "quantity": quantity, "total": total}
                )
                print("Sale total: BDT", total)

            else:
                print("Unknown option")

        except (ValueError, TypeError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
