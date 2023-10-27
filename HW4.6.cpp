
stack_enque = Stack()  // Stack for enqueue operations
stack_deque = Stack()  // Stack for dequeue operations

    enqueue(item): // here we are inserting the item inside the que 
        stack_in.push(item)

    dequeue(): //here we are deque the element from the que
        if stack_out.isEmpty(): // checking that stack is empoty or not
            while not stack_in.isEmpty(): //idf the stack is not empty 
                stack_out.push(stack_in.pop()) // pop item from stack_eque to the and push into it stack_deque
        if stack_out.isEmpty():
            raise EmptyQueueException("Queue is empty") // if stack_deque is empty then notify the user
        return stack_out.pop()
