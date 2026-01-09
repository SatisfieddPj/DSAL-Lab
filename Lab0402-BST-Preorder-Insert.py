"""
Docstring for Lab0402-BST-Preorder-Insert
"""

class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left
    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right
    def set_right(self,right):
        self.right = right
 
class BST:
    def __init__(self, data=None):
        self.root = data

    def get_root(self):
        return self.root
    def set_root(self, root):
        self.root = root
        out = self.root
        print(out.data)
    
    def insert(self, data):
        new_bstNode = BSTNode(data)
        current = self.root

        print(self.root)

def main():
    bst = BST()
    data1 = BSTNode(5)
    data2 = BSTNode(10)
    data3 = BSTNode(6)
    bst.set_root(data1)
    
    # bst.insert(data1)
    # bst.insert(data2)
    # bst.insert(data3)
main()