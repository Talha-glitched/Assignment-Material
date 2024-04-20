class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_tree(root):
    if root is None:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Example tree:
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("BFS Traversal for tree:", bfs_tree(root))
def dfs_tree(root):
    if root is None:
        return []
    
    result = []
    
    def dfs(node):
        if node is None:
            return
        result.append(node.value)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result

print("DFS Traversal for tree:", dfs_tree(root))