import ast

class BubbleSort:
    def __init__(self):
        self.comparison_count = 0

    def bubbleSort(self, data_list, last):
        self.comparison_count = 0

        current = 0

        is_sorted = False
        
        while current <= last and is_sorted is False:
            walker = last
            
            is_sorted = True
            
            while walker > current:
                self.comparison_count += 1

                if data_list[walker] < data_list[walker - 1]:

                    is_sorted = False
                    
                    data_list[walker], data_list[walker - 1] = data_list[walker - 1], data_list[walker]

                walker -= 1
            
            print(data_list)

            current += 1
            
        print(f"Comparison times: {self.comparison_count}")


data = ast.literal_eval(input())
last_idx = int(input())

sorter = BubbleSort()
sorter.bubbleSort(data, last_idx)