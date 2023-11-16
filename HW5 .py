function inorder (node): 
  stack = [] #It is empty list, which will serve as a stack to keep track of nodes to be procced. 
  current = node #It is pointer initilized with node passsed an argument. 
  while current or stack: 
    if current: #This statement checks if the current i not none. If its none, it means there is a node to process in the current subtree.
      stack.append(current) #If 'current' is not 'None', it means there is a node to process. 
      current = current.left #The current node is pushed onto the 'stack', effectively storing it for future processing.
      #current is updated to its left child, stimulating a move to the left subtree.
    else: #If current is none, it means you have reached the leftmost leaft node in the current subtree, and there are no more left children to explore.
      current = stack.pop() #The most recent node that was pushed onto the 'stack' is poped and asigned to the 'current' variable. This node is the present of the previously process leaf node.
      print(current.data) # The 'data' of the 'current' node is printed. This line represents the processing of the current node. 
      #you replace print(current_node) with any operation you wnt to perform on the node, such as collecting values or performing specific tasks.
      current = current.right #After processing the 'current' node, you update 'current' ot its right child. This simulates the transversal of the right subtree.
  return