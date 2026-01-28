class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def traverse(self):
        if self.count == 0: # Empty List, No Data
            print("This is an empty list.")
        else: # Have Data
            current = self.head
            while current is not None:
                print(current.data, end="")
                if current.next is not None:
                    print(" -> ", end="")
                current = current.next

    def insert_last(self, data):
        new_node = DataNode(data)

        if not self.head: # Empty List, Add data to head
            self.head = new_node

        else: # Not an Empty List, Add DataNode to the last
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def insert_front(self, data):
            new_node = DataNode(data)
            new_node.next = self.head # attach head to the next of the new_node
            self.head = new_node
            self.count += 1
    
    def insert_before(self, target_data, new_data):
        new_node = DataNode(new_data)

        if not self.head:# Empty List, Cannot add something before nothing
            print("Cannot insert,", target_data, "does not exist.")
            return
        
        if self.head.data == target_data: # If the target is the head itself, just insert_front
            self.insert_front(new_data)
            return
        
        # if not any of the above, find the target
        current = self.head
        while current.next and current.next.data != target_data:
            current = current.next

        if current.next and current.next.data == target_data: # found target! insert before it (attach the target to new_node)
            new_node.next = current.next
            current.next = new_node
            self.count += 1
        else:
            print("Cannot insert,", target_data, "does not exist.")


def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #    mylist.delete(data)
    else:
        print("Invalid Condition!")
  mylist.traverse()

main()