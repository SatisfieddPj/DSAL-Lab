"""Copy Stack"""

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

    def is_empty(self):
        """empty mai?"""
        if self.size == 0:
            return True
        else:
            return False

    def get_stack_top(self):
        """who is on the top"""
        if self.size != 0:
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
        
    def get_size(self):
        """how big big"""
        return self.size

    def print_stack(self):
        """just print"""
        print(self.data)

def copy_stack(stack1, stack2):
    """copy one data stack to another"""
    stack2.data = stack1.data.copy()
    stack2.size = stack1.size
    return stack2.data

def print_status():
    """Print all stacks"""
    print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
    STACK1_.print_stack()
    print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
    STACK2_.print_stack()
    print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
    STACK3_.print_stack()
    print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
    STACK4_.print_stack()
    print()

STACK1_ = ArrayStack()
STACK2_ = ArrayStack()

STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

# เพิ่มข้อมูลใน Stack1
for _ in range(int(input())):
  STACK1_.push(input())

# เพิ่มข้อมูลใน Stack2
for _ in range(int(input())):
  STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_),
  TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))