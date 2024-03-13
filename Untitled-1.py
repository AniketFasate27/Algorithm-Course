MAX-HEAP-DELETE(A, x):
    if A.heap-size < 1:
        error "Heap underflow"
    index = MAP-GET-INDEX(x)    // Assume this retrieves the index of x in O(1) time
    if index == A.heap-size:
        A.heap-size = A.heap-size - 1
        return x
    removed_element = A[index]
    A[index] = A[A.heap-size]
    A.heap-size = A.heap-size - 1
    if A[index] > removed_element:
        MAX-HEAPIFY-UP(A, index)
    else:
        MAX-HEAPIFY(A, index)
    return removed_element