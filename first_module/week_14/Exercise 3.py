class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root:Node = None 

    def print_structure(self):
        string =  self._print_structure(self.root)
        print(string)

    def _print_structure(self, node:Node, string:str=""):      
        if node is not None:
            string += f"{str(node.data)}-" 
            string = self._print_structure(node.left, string)
            string = self._print_structure(node.right, string)
        return string
    
if __name__ == '__main__':
    three = BinaryTree()
    three.root = Node(0)
    three.root.left = Node(1)
    three.root.right =  Node(2)
    three.root.left.left = Node(3)
    three.root.left.right = Node(4)
    three.root.right.left = Node(5)
    three.root.right.right = Node(6)
    three.print_structure()