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
    
    def insert(self, data):
        new_bstNode = BSTNode(data)
        current = self.root
        value = int(data)
        
        if current == None :
            self.set_root(new_bstNode)
            return

        while True:
            if value < int(current.get_data()):
                if current.get_left() == None:
                    current.set_left(new_bstNode)
                    break
                else:
                    current = current.get_left()
            else:
                if current.get_right() == None:
                    current.set_right(new_bstNode)
                    break
                else:
                    current = current.get_right()
    def preorder(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node == None:
            return
        
        print(f"->", node.get_data(), end=" ")
        self._preorder_recursive(node.get_left())
        self._preorder_recursive(node.get_right())

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()