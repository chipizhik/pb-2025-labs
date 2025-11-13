flights = [
    {"flight": "A1", "departure": 9, "arrival": 12},
    {"flight": "B2", "departure": 14, "arrival": 18},
    {"flight": "C3", "departure": 6, "arrival": 8}
]

filtered_flights = list(filter(lambda xz: xz["arrival"] < 12, flights))

for flight in filtered_flights:
    print(flight)