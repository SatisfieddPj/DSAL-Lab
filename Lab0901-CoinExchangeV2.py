import json

def coinExchangeV2(amount, coins_dict):
    # สร้างตาราง DP เริ่มต้นด้วยค่าที่สื่อว่าเป็นไปไม่ได้ (Infinity)
    # dp[i] เก็บจำนวนเหรียญที่น้อยที่สุดเพื่อให้ได้เงินรวม i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # parent[i] เก็บ (มูลค่าเหรียญที่เลือก, ตำแหน่งก่อนหน้า) เพื่อใช้แกะรอย
    parent = [None] * (amount + 1)
    
    # แปลง dict ให้เป็นรายการเหรียญทั้งหมดที่มี (เช่น {13: 2} -> [13, 13])
    # เรียงจากมากไปน้อยเพื่อให้ผลลัพธ์การแกะรอยสม่ำเสมอ
    sorted_denominations = sorted(coins_dict.keys(), key=int, reverse=True)
    
    # วนลูปตามจำนวนเหรียญที่มีจริง ๆ
    for coin_val in sorted_denominations:
        coin_val_int = int(coin_val)
        count = coins_dict[coin_val]
        
        # สำหรับเหรียญแต่ละชิ้นที่มี
        for _ in range(count):
            # วนลูปถอยหลังจาก amount ลงมาถึง coin_val เพื่อป้องกันการใช้เหรียญซ้ำใบเดิม
            for i in range(amount, coin_val_int - 1, -1):
                if dp[i - coin_val_int] + 1 < dp[i]:
                    dp[i] = dp[i - coin_val_int] + 1
                    parent[i] = (coin_val_int, i - coin_val_int)

    # ตรวจสอบว่าสามารถทอนได้หรือไม่
    if dp[amount] == float('inf'):
        return None

    # แกะรอยหาว่าใช้เหรียญแต่ละชนิดไปกี่เหรียญ
    used_counts = {int(k): 0 for k in coins_dict.keys()}
    curr = amount
    while curr > 0:
        coin_val, prev = parent[curr]
        used_counts[coin_val] += 1
        curr = prev
        
    return used_counts

def main():
    # รับ Input ตาม Specification
    try:
        amount_input = input().strip()
        if not amount_input: return
        amount = int(amount_input)
        
        coins_json = input().strip()
        coins_dict = json.loads(coins_json)
        
        # คำนวณ
        result = coinExchangeV2(amount, coins_dict)
        
        # แสดงผลตาม Specification
        print(f"Amount: {amount}")
        if result is None:
            print("Can not exchange.")
        else:
            print("Coin exchange result:")
            total_coins = 0
            # แสดงผลเรียงจากเหรียญมูลค่ามากไปน้อยตามตัวอย่าง
            for coin in sorted(result.keys(), reverse=True):
                cnt = result[coin]
                print(f"  {coin} baht = {cnt} coins")
                total_coins += cnt
            print(f"Number of coins: {total_coins}")
            
    except (ValueError, json.JSONDecodeError):
        # กรณี Input ผิดพลาด แต่โจทย์ไม่ได้ระบุให้แสดง Error เฉพาะเจาะจง
        pass

if __name__ == "__main__":
    main()