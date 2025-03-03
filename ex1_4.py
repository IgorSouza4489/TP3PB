class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    def _is_valid_bst_recursive(self, node, min_value, max_value):
        if node is None:
            return True
        if not (min_value < node.value < max_value):
            return False
        return (self._is_valid_bst_recursive(node.left, min_value, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_value))
    
bst = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)
print("A árvore é uma BST válida?", bst.is_valid_bst()) 
bst.root.left.right.value = 55  
print("A árvore é uma BST válida?", bst.is_valid_bst())  
