import json

class Student:
    def __init__(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_name(self):
        return self.__name

    def print_details(self):
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.2f}")

def binary_search(data, name):
    low = 0
    high = len(data) - 1
    count = 0
    
    while low <= high:
        count += 1
        mid = (low + high) // 2
        mid_name = data[mid].get_name()
        
        if mid_name == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {count}")
            return
        elif mid_name < name:
            low = mid + 1
        else:
            high = mid - 1
            
    print(f"{name} does not exists.")
    print(f"Comparisons times: {count}")

def main():
    try:
        json_str = input().strip()
        target_name = input().strip()
        
        raw_data = json.loads(json_str)
        student_list = []
        
        for item in raw_data:
            s_id = item.get("ID") if "ID" in item else item.get("id")
            s_name = item.get("Name") if "Name" in item else item.get("name")
            s_gpa = item.get("GPA") if "GPA" in item else item.get("gpa")
            
            student_list.append(Student(s_id, s_name, s_gpa))
        
        binary_search(student_list, target_name)
    except EOFError:
        pass

if __name__ == "__main__":
    main()