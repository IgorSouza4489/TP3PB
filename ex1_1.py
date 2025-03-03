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
    def preorder_traversal(self):
        result = []
        self._preorder_helper(self.root, result)
        return result
    def _preorder_helper(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)
    def postorder_traversal(self):
        result = []
        self._postorder_helper(self.root, result)
        return result
    def _postorder_helper(self, node, result):
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.value)
            
bst = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)
print("In-order:", bst.inorder_traversal())  
print("Pre-order:", bst.preorder_traversal()) 
print("Post-order:", bst.postorder_traversal()) 
