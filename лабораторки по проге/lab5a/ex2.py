purchases = [
    {"item": "Laptop", "price": 1000, "quantity": 2},
    {"item": "Mouse", "price": 25, "quantity": 5},
    {"item": "Keyboard", "price": 45, "quantity": 3}
]
total_costs = list(map(lambda purchase: (purchase['item'], purchase['price'] * purchase['quantity']), purchases))
most_expensive = max(total_costs, key=lambda item: item[1])

print("Общие стоимости:", total_costs)
print("Самая дорогая покупка:", most_expensive)