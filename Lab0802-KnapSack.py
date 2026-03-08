import json

class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_cost(self):
        """Value density for greedy selection."""
        return self.price / self.weight if self.weight > 0 else 0

def fmt_num(n):
    """Removes .0 from whole numbers, keeping others as is."""
    return int(n) if n == int(n) else n

def knapsack(items, capacity):
    print(f"Knapsack Size: {capacity} kg")
    print("=" * 31)

    remaining = capacity
    total_price = 0.0
    
    # Sort: Cost DESC, then Index ASC (tie-breaker)
    # enumerate gives us (index, item)
    sorted_items = sorted(
        enumerate(items), 
        key=lambda x: (-x[1].get_cost(), x[0])
    )

    for _, item in sorted_items:
        if item.weight <= remaining + 1e-9:
            # Pick the item
            p_display = fmt_num(item.price)
            w_display = fmt_num(item.weight)
            
            print(f"{item.name} -> {w_display} kg -> {p_display} THB")
            
            total_price += item.price
            remaining -= item.weight

    print(f"Total: {fmt_num(total_price)} THB")

def main():
    # Read number of items
    line = input().strip()
    if not line: return
    num_items = int(line)

    items = []
    for _ in range(num_items):
        data = json.loads(input().strip())
        # Use .get() for safety without try-except
        items.append(Item(
            data.get('name', 'Item'),
            data.get('price', 0),
            data.get('weight', 0)
        ))

    # Read capacity
    cap_line = input().strip()
    if cap_line:
        knapsack(items, float(cap_line))

main()