import numpy as np

keys = [0, 1, 2, 3, 4, 5, 6, 7]
probabilities = [0.0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14] 
dummy_probs = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05]

# Manually construct a suboptimal BST 
bst = {
    4: {"left": 2, "right": 5},
    2: {"left": 0, "right": 3}, 
    5: {"left": 1, "right": 6},
    6: {"right": 7}  
}

def search_cost(tree, probabilities):
    cost = 0
    for i, key in enumerate(keys):
        level = get_depth(tree, key) 
        cost += level * probabilities[i]  
    return cost
        
def get_depth(tree, key):
    depth = 0
    curr = tree[4] # start at root
      
    while curr:
       if key < curr["left"]:
           curr = tree[curr["left"]]
           depth += 1
       elif key > curr["right"]:
           curr = tree[curr["right"]]  
           depth += 1
       else:
           return depth 
           
    return float("inf") # key not present

total_cost = search_cost(bst, probabilities) 
# Total cost = 3.12
print(total_cost)