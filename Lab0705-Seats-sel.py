import ast

class SeatSorter:
    def __init__(self):
        self.comparison_count = 0

    def is_less_than(self, seat1, seat2):
        char1, num1 = seat1[0], int(seat1[1:])
        char2, num2 = seat2[0], int(seat2[1:])
        
        if char1 < char2:
            return True
        elif char1 == char2:
            return num1 < num2
        return False

    def selectionSort(self, data_list, last):
        self.comparison_count = 0
        current = 0
        
        while current < last:
            smallest = current
            walker = current + 1
            
            while walker <= last:
                self.comparison_count += 1
                
                if self.is_less_than(data_list[walker], data_list[smallest]):
                    smallest = walker
                
                walker += 1

            data_list[current], data_list[smallest] = data_list[smallest], data_list[current]
            
            print(data_list)
            
            current += 1
            
        print(f"Comparison times: {self.comparison_count}")


data = ast.literal_eval(input())
last_idx = int(input())

sorter = SeatSorter()
sorter.selectionSort(data, last_idx)