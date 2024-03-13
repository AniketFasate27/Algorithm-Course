Function max-heapify(A,i)
while true
    l = LEFT(i) #compute the index of the ledt child 
    r = RIGHT(i) #compute the index of the right child
    largest = i
    #check if left child exits ad is greater tahn current node
    if l <= A.heap_size and A[l] > A[i]:
        largest = 1
    else largest = i
    # check if right child exits and is greater than the largest so far 
    if r <= A.heap and A[r] > A[largest]:
        largest = r
    #if the largest is not the current noode, then weill swap them
    if (largest != i):
        exchange A[i] with A[largest]
        i = largest # upadinf i to continue down the heap
    else
        break #max - heap property is satisfied, exit the loop