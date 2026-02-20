import ast

class InsertionSort:
    def __init__(self):
        self.comparison_count = 0

    def insertionSort(self, data_list, last):
        self.comparison_count = 0
        
        current = 1
        
        # วนลูปจนถึง index สุดท้าย (last)
        while current <= last:
            hold = data_list[current]
            walker = current - 1
            
            # ลูปเพื่อหาตำแหน่งที่จะแทรก
            while walker >= 0:
                self.comparison_count += 1 # นับครั้งที่เปรียบเทียบ
                
                if hold < data_list[walker]:
                    data_list[walker + 1] = data_list[walker]
                    walker -= 1
                else:
                    # ถ้าเจอค่าที่น้อยกว่าหรือเท่ากัน ให้หยุด
                    break
            
            data_list[walker + 1] = hold
            
            # แสดงผล List หลังจากแทรกข้อมูลในแต่ละรอบ
            print(data_list)
            
            current += 1
            
        print(f"Comparison times: {self.comparison_count}")


# if __name__ == "__main__": # ถ้ารันด้วยตัวเองให้รันบล็อกนี้ แต่ถ้าโดนยืมไป ไม่ต้อง (Gemini สอนมา)
#     try:
#         # รับค่าลิสต์ เช่น [23, 78, 45, 8, 32, 56]
#         input_list_str = input() 
#         # ใช้ ast.literal_eval เพื่อแปลง string เป็น list ของตัวเลขอย่างปลอดภัย
#         data = ast.literal_eval(input_list_str)
        
#         # รับค่า last index เช่น 5
#         last_idx = int(input())
        
#         # สร้าง Object และสั่ง Sort
#         sorter = InsertionSort()
#         sorter.insertionSort(data, last_idx)
        
#     except Exception as e:
#         print("Error: โปรดกรอกข้อมูลให้ตรงตามรูปแบบที่กำหนด (เช่น [1, 2, 3] และตัวเลข index)")


# รับ input แบบดิบๆ เลย (ถ้าพิมพ์ผิด โปรแกรมจะ Error ทันที)
data = ast.literal_eval(input())
last_idx = int(input())

# เรียกใช้งาน
sorter = InsertionSort()
sorter.insertionSort(data, last_idx)