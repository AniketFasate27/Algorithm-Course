function RANDOMIZED_SELECT(A, p, r, i):
    while(p != r){ 
        q = RANDOMIZED_PARTITION(A, p, r) // Partition the array and get the pivot index q
        k = q - p + 1 // Calculate the number of elements in the lower subarray including the pivot
        if(i == k){ 
            return A[q] // If i is equal to k, pivot is the i-th smallest element
        } else if(i < k){ 
            r = q - 1 // If i is less than k, search in the left subarray
        } else { 
            p = q + 1 // If i is greater than k, search in the right subarray
            i = i - k // Adjust i for the new subarray
        } 
    } 
    return A[q] // When p equals r, the element at position q is the i-th smallest
