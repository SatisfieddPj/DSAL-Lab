"""
Docstring for SinglyLinkedList
"""
class DataNode:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class SinglyLinkedList :
    def __init__(self, data=None):
        self.count = 0
        self.head = DataNode(data)

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
        current = self.head
        new_node = DataNode(data)

        if self.count == 0: # Empty List, Add data to head
            self.head = new_node
            #print("add new node to the head; Head ->", current.data)
        else: # Not an Empty List, Add DataNode to the last
            while current.next is not None: # If the next one isn't None meaning it's not the last one
                current = current.next
            current.next = new_node
            #print("add new node to the last; Last ->", current.data)
        self.count += 1


def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()

main()