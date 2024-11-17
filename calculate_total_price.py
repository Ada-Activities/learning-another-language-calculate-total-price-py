def calculate_total_price(order):
    total = 0

    for item in order:
        total += item["price"]

    return total


my_order = [
    {
        "entre": "Fish Tacos",
        "price": 14.97,
    },
    {
        "entre": "Vegan Spaghetti",
        "price": 21.47,
    },
]

my_total = calculate_total_price(my_order)
print(f"The total is ${my_total}")
