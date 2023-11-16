Function Queue (head, tail):
#attribute which will store the NULL when linked list is empty 
    head = NULL 
    tail = NULL 

Function ENQUEUE(Queue, data): 
# I sthe opertion which will adds a new node containing the data 
# to the end of the queueue and updates the tail pointer accordingly 
# If the queue is initially empty, it also sets the head pointer to the new node.

    new_node = Node(data) #creat the node with given value
    if head is NULL: # if the que is empty, set the head and the tail to the new node
        head = new_node
        tail = new_node
        #if not then set the next pointer of the tail node to the new node an dupdate the tail pointer
    else:      
        tail.next = new_node
        tail = new_node
# Here function deuque removes the front node from the queue and return its data.
#Then after returning the data it will updates the ghead pointer to the next eleemnt in the queue.
#After the process if there is no element is left in the queue then it ewill return the ytail pointer to the NULL.

Function DEQUEUE(Queue):
#if the queue is empty then retrun the null
    if head is NULL:
        return NULL
#if no then srytore the value of the node nad update the head pointer to the next node
    else:
        data = head.data
        head = head.next
#if the queueue in empty now then we will set the tail pointer to null
        if head is NULL:
            tail = NULL
# Return the data of the dequed noe
        return data

#By using the head and tail attributes implementation of the enqueue and dequeue operation ensures the 
#time complexity of the O(1).
