"""
Docstring for Lab0205-Student-Grp
"""

class ArrayStack:
    def __init__(self):
        """initial"""
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """pop pop pop"""
        if self.size != 0:
            self.size -=1
            return self.data.pop()
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """empty mai?"""
        if self.size == 0:
            return True
        else:
            return False

    def get_stack_top(self):
        """who is on the top"""
        if self.size != 0:
            return str(self.data[-1])
        else:
            return print("Underflow: Cannot get stack top from an empty list")
        
    def get_size(self):
        """how big big"""
        return self.size

    def print_stack(self):
        """just print"""
        print(self.data)


m = int(input()) # number of groups
n = int(input()) # number of students

