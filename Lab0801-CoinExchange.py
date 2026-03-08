import json

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def coin_exchange(amount, coins_inventory):
    result = {}
    remaining = amount
    
    available_denominations = sorted(coins_inventory.keys(), reverse=True)

    for coin in available_denominations:
        have = coins_inventory.get(coin, 0)
        if have <= 0:
            result[coin] = 0
            continue
            
        need = remaining // coin
        use = min(need, have)
        
        result[coin] = use
        remaining -= use * coin

    return result if remaining == 0 else None

def main():
    try:
        # Input
        raw_amount = input("Enter amount: ").strip()
        if not raw_amount: return
        amount = int(raw_amount)
        
        raw_json = input("Enter coins inventory (JSON format): ").strip()
        inventory = convert_key(json.loads(raw_json))

        # Calculation
        used = coin_exchange(amount, inventory)

        # Output
        print(f"Amount: {amount}")
        if used is None:
            print("Coins are not enough.")
        else:
            print("Coin exchange result:")
            total_count = 0
            # Sort for clean display
            for coin in sorted(used.keys(), reverse=True):
                count = used[coin]
                print(f"  {coin:>1} baht = {count} coins")
                total_count += count
            print(f"Number of coins: {total_count}")
            
    except ValueError:
        print("Error: Please enter a valid number for the amount.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format for coins.")

main()