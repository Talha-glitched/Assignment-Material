import random
import time
import pandas as pd
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_unique_numbers(start, end, count):
    return random.sample(range(start, end), count)

def build_tree(numbers):
    root = None
    for num in numbers:
        root = insert(root, num)
    return root

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def bfs(root, goal):
    if root is None:
        return None
    
    queue = [(root, [root.value])]
    
    while queue:
        node, path = queue.pop(0)
        if node.value == goal:
            return path
        if node.left:
            queue.append((node.left, path + [node.left.value]))
        if node.right:
            queue.append((node.right, path + [node.right.value]))
    return None

def dfs(root, goal):
    if root is None:
        return None
    
    stack = [(root, [root.value])]
    
    while stack:
        node, path = stack.pop()
        if node.value == goal:
            return path
        if node.right:
            stack.append((node.right, path + [node.right.value]))
        if node.left:
            stack.append((node.left, path + [node.left.value]))
    return None

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Generate random and unique numbers for each set
input_sizes = [1000, 40000, 80000, 200000, 1000000]
sets_of_numbers = {size: generate_unique_numbers(1, 10*size, size) for size in input_sizes}

# Define the goal index
goal_index = {size: len(numbers) - 220 for size, numbers in sets_of_numbers.items()}

# Execute BFS and DFS for each set and measure time
results = []
for size, numbers in sets_of_numbers.items():
    root = build_tree(numbers)
    goal = numbers[goal_index[size]]
    
    bfs_result, bfs_time = measure_time(bfs, root, goal)
    dfs_result, dfs_time = measure_time(dfs, root, goal)
    
    results.append({'Input Size': size, 'BFS Time': bfs_time, 'DFS Time': dfs_time})

# Create dataframe
df = pd.DataFrame(results)

# Plot the bar chart
df.plot(kind='bar', x='Input Size', y=['BFS Time', 'DFS Time'], figsize=(10, 6))
plt.title('Time taken by BFS and DFS for different input sizes')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.xticks(rotation=45)
plt.show()
