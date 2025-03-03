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

    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None  
        
            if node.left is None:
                return node.right  
            elif node.right is None:
                return node.left  
            successor = self._min_value_node(node.right)
            node.value = successor.value  
            node.right = self._delete_recursive(node.right, successor.value)  

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

bst = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("In-order antes da remoção:", bst.inorder_traversal())
bst.delete(20)
print("In-order após remover 20:", bst.inorder_traversal())
bst.delete(30)
print("In-order após remover 30:", bst.inorder_traversal())
bst.delete(50)
print("In-order após remover 50:", bst.inorder_traversal())
