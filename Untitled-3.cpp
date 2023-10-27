ITERATIVE_RANDOMIZED_SELECT(A, p, r, k):
//  "A" is the input aaray
// "p" is represnt the starting point of the current subarray.
// It initially started as left end point of entire array. 
// "1r" is is the notation useed for the variable represent the ending index of the subarray.
// It initially starts as the right endpoint of the enire array, 
// "k" represnts the position of the ellemnt that you want to find.
// here value k =0 represents the smallest element and k =1 represents the second smallest and so on
//"q" This variable is used to store the pivot position of the after the array. 
// the array is partitioned by the "RANDOMIZED_PARTITION" function. 
// Its represents the position of the pivot element in current subarray.
    while p < r:
        q = RANDOMIZED_PARTITION(A, p, r)  // Partition the array and get the pivot position q

        if k == q:
            return A[q]  // Found the kth smallest element
        else if k < q:
            r = q - 1  // Recurse on the left subarray
        else:
            p = q + 1  // Recurse on the right subarray

    return A[p]  // Return the element at position p (kth smallest element)
