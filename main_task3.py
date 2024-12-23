#сложность алгоритма O(n)

class BinaryTree:
    class Node:
        def __init__(self,value):
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
        
    def preorder(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)
        
    def swap(self, root):
        if root is None:
            return
        if root.left is None or root.right is None:
            return

        if root.left.value < root.right.value:
            temp = root.left
            root.left = root.right
            root.right = temp
            
    def invertBinaryTree(self, root):
        if root is None:
            return
        self.swap(root)
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        
         

root = BinaryTree.Node(2)
root.left = BinaryTree.Node(8)
root.right = BinaryTree.Node(22)
root.left.left = BinaryTree.Node(53)
root.left.right = BinaryTree.Node(34)
root.right.left = BinaryTree.Node(9)
root.right.right = BinaryTree.Node(3)
tree = BinaryTree()
tree.invertBinaryTree(root)
tree.preorder(root)
