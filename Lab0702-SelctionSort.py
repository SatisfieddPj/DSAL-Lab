import ast

class SelectionSort:
    def __init__(self):
        self.comparison_count = 0

    def selectionSort(self, data_list, last):
        self.comparison_count = 0
        
        current = 0
        
        while current < last:
            smallest = current
            
            walker = current + 1
            
            while walker <= last:
                # นับจำนวนการเปรียบเทียบข้อมูล
                self.comparison_count += 1
                
                if data_list[walker] < data_list[smallest]:

                    smallest = walker
                
                walker += 1
            
            # 5. exchange (current, smallest)
            data_list[current], data_list[smallest] = data_list[smallest], data_list[current]
            
            # แสดงผล
            print(data_list)
            
            current += 1
            
        print(f"Comparison times: {self.comparison_count}")


data = ast.literal_eval(input())
last_idx = int(input())

sorter = SelectionSort()
sorter.selectionSort(data, last_idx)