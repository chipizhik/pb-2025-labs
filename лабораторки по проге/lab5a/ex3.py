clients = [
    {"name": "Alice", "income": 49999},
    {"name": "Bob", "income": 120000},
    {"name": "Charlie", "income": 70000}
]

clientsFilter = list(map(
    lambda client: {
        **client, "category": "High" if client["income"] > 100000
                  else "Medium" if client["income"] >= 50000
                  else "Low"
    },
    clients
))
for client in clientsFilter:
    print(client)
