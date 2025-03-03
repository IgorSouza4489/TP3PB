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
    def search(self, value):
        return self._search_recursive(self.root, value)
    def _search_recursive(self, node, value):
        if node is None:
            return False  
        if node.value == value:
            return True  

        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

bst = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)
valor_procurado = 40
encontrado = bst.search(valor_procurado)
if encontrado:
    print(f"Valor {valor_procurado} encontrado na árvore!")
else:
    print(f"Valor {valor_procurado} NÃO encontrado na árvore.")
