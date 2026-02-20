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

    def insertionSort(self, data_list, last):
        self.comparison_count = 0
        current = 1
        
        while current <= last:
            hold = data_list[current]
            walker = current - 1
            
            while walker >= 0:
                self.comparison_count += 1

                if self.is_less_than(hold, data_list[walker]):
                    data_list[walker + 1] = data_list[walker]
                    walker -= 1
                else:
                    break
            
            data_list[walker + 1] = hold
            print(data_list)
            current += 1
            
        print(f"Comparison times: {self.comparison_count}")


data = ast.literal_eval(input())
last_idx = int(input())

sorter = SeatSorter()
sorter.insertionSort(data, last_idx)