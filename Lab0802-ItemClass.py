import json

class Item:
    def __init__(self, name, price, weight):
        self.name = str(name)

        self.price = float(price) if isinstance(price, (int, float)) else 0.0
        self.weight = float(weight) if isinstance(weight, (int, float)) else 0.0

    def format_num(self, n):
        """Removes .0 if the number is a whole number."""
        return int(n) if n == int(n) else n

    def get_cost(self):
        if self.weight <= 0:
            return 0
        cost = self.price / self.weight
        return self.format_num(cost)

    def __str__(self):
        # Using format_num to clean up the output
        p = self.format_num(self.price)
        w = self.format_num(self.weight)
        return f"{self.name}\n{p}\n{w}"

def main():
    user_input = input().strip()
    if not user_input:
        return

    item_in = json.loads(user_input)
    
    # Safe retrieval without try-except
    item = Item(
        item_in.get("name", "Unknown"), 
        item_in.get("price", 0), 
        item_in.get("weight", 0)
    )

    print(item)

main()