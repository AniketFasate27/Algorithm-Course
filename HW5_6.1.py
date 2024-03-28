function inorder_tree_walk(node):
    stack = []  # An empty list that serves as a stack to keep track of nodes
    current = node  # A pointer initialized with the node passed as an argument

    while current or stack:  # Continue until both current is None and the stack is empty.
        if current:
            stack.append(current)  # Push the current node onto the stack
            current = current.left  # Move to the left child
        else:
            current = stack.pop()  # Pop the node from the stack
            print(current.data)  # Process the node data
            current = current.right  # Move to the right child
