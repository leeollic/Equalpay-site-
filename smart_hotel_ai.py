class SmartHotelAI:
    def __init__(self):
        self.rooms = [
            {"number": 101, "type": "Single", "price": 50, "rating": 3},
            {"number": 201, "type": "Double", "price": 80, "rating": 4},
            {"number": 301, "type": "Suite", "price": 150, "rating": 5},
        ]

    def recommend_room(self, budget, preference):
        best_room = None
        best_score = -1

        for room in self.rooms:
            if room["price"] <= budget:
                score = 0

                # AI-like scoring system
                if preference == "cheap":
                    score = 100 - room["price"]
                elif preference == "luxury":
                    score = room["rating"] * 20
                elif preference == "balanced":
                    score = (room["rating"] * 10) - (room["price"] / 10)

                if score > best_score:
                    best_score = score
                    best_room = room

        return best_room


# DEMO
ai = SmartHotelAI()

budget = 100
preference = "balanced"

result = ai.recommend_room(budget, preference)

if result:
    print(f"Recommended Room: {result['number']}")
    print(f"Type: {result['type']}")
    print(f"Price: ${result['price']}")
else:
    print("No suitable rooms found.")
