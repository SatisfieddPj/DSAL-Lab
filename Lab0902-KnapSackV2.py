import json

def knapsackV2(capacity, itemList):
    # n คือจำนวนสินค้าทั้งหมด
    n = len(itemList)
    
    # สร้างตาราง DP เพื่อเก็บค่ามูลค่าสูงสุดที่น้ำหนักต่างๆ
    # dp[i][w] คือมูลค่าสูงสุดที่ได้จากสินค้า i ชิ้นแรก เมื่อน้ำหนักไม่เกิน w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # เริ่มเติมตาราง DP
    for i in range(1, n + 1):
        name, price, weight = itemList[i-1]
        for w in range(capacity + 1):
            if weight <= w:
                # เลือกสิ่งที่คุ้มที่สุดระหว่าง "ไม่หยิบชิ้นนี้" กับ "หยิบชิ้นนี้"
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + price)
            else:
                # ถ้าน้ำหนักเกินกระเป๋า ต้องไม่หยิบชิ้นนี้
                dp[i][w] = dp[i-1][w]

    # แกะรอย (Backtracking) เพื่อหาว่าหยิบสินค้าชิ้นไหนบ้าง
    chosen_items = []
    w = capacity
    for i in range(n, 0, -1):
        # ถ้าค่าในตารางเปลี่ยนไป แสดงว่าเราเลือกหยิบสินค้าชิ้นที่ i
        if dp[i][w] != dp[i-1][w]:
            item = itemList[i-1]
            chosen_items.append(item)
            w -= item[2] # ลบน้ำหนักของสินค้าที่เลือกออก

    # เรียงลำดับชื่อสินค้าที่เลือกจาก A - Z ตามเงื่อนไข
    chosen_items.sort(key=lambda x: x[0])
    
    # แสดงผลตาม Output Specification
    print(f"Total: {dp[n][capacity]}")
    for name, price, weight in chosen_items:
        # พิมพ์ ชื่อ -> น้ำหนัก -> ราคา
        print(f"{name} -> {weight} kg -> {price} THB")

def main():
    # รับ Input ตาม Specification: บรรทัดแรกเป็น List สินค้า, บรรทัดที่สองคือน้ำหนัก
    raw_list = input().strip()
    raw_capacity = input().strip()
    
    if not raw_list or not raw_capacity:
        return

    # แปลง input โดยใช้ json.loads ตามคำแนะนำในโจทย์
    itemList = json.loads(raw_list)
    capacity = int(raw_capacity)
    
    knapsackV2(capacity, itemList)

main()