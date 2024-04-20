import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def minimax(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or len(node.children) == 0:
        return node.value
    
    if maximizingPlayer:
        maxEval = -math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

# Example usage
root = Node()
root.children = [Node(3), Node(6), Node(2)]
root.children[0].children = [Node(5), Node(9), Node(1)]
root.children[1].children = [Node(2), Node(8), Node(4)]
root.children[2].children = [Node(6), Node(7), Node(3)]

alpha = -math.inf
beta = math.inf
maximizingPlayer = True
depth = 3

print("Minimax value:", minimax(root, depth, alpha, beta, maximizingPlayer))
