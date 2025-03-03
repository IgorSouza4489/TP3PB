import threading

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class ParallelSearch:
    def __init__(self):
        self.found = threading.Event() 
        self.lock = threading.Lock()   
    def search(self, node, target):
        if node is None or self.found.is_set():
            return  
        if node.value == target:
            with self.lock:
                self.found.set()  
            return
        left_thread = threading.Thread(target=self.search, args=(node.left, target))
        right_thread = threading.Thread(target=self.search, args=(node.right, target))
        left_thread.start()
        right_thread.start()
        left_thread.join()
        right_thread.join()
        
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)
parallel_search = ParallelSearch()
parallel_search.search(root, 60)
if parallel_search.found.is_set():
    print("Valor encontrado!")
else:
    print("Valor não encontrado.")
