"""
Docstring for Lab0404-BST-Min-Max
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
    
    def is_empty(self):
        return (self.get_root() == None)
    
    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node == None:
            return
        
        self._inorder_recursive(node.get_left())
        print(f"->", node.get_data(), end=" ")
        self._inorder_recursive(node.get_right())
    
    def postorder(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node == None:
            return
        
        self._postorder_recursive(node.get_left())
        self._postorder_recursive(node.get_right())
        print(f"->", node.get_data(), end=" ")

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
        else:
            print("Preorder: ", end="")
            self.preorder()
            print("\nInorder: ", end="")
            self.inorder()
            print("\nPostorder: ", end="")
            self.postorder()
            print()
    
    def find_min(self):
        if self.root == None:
            return None
        current = self.root

        while current.get_left() != None:
            current = current.get_left()
        return current.get_data()

    def find_max(self):
        if self.root == None:
            return None
        current = self.root

        while current.get_right() != None:
            current = current.get_right()
        return current.get_data()

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()