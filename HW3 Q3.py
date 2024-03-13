function PARTITION’(A, p, r)
    x = A[r]   // Set pivot element
    i = p - 1  // Initialize index for elements less than pivot
    k = r      // Initialize index for elements greater than pivot, start from the end

    j = p
    while j <= k do   // Iterate through elements
        if A[j] < x then    // If current element is less than pivot
            i = i + 1
            exchange A[i] with A[j]  // Move elements less than pivot to the left side
            j = j + 1
        elif A[j] > x then    // If current element is greater than pivot
            k = k - 1
            exchange A[k] with A[j]  // Move elements greater than pivot to the right side
            // Do not increment j because the swapped element from A[k] needs to be checked
        else    // If current element is equal to pivot
            j = j + 1   // Simply move to the next element
        end if
    end while

    // At this point, i marks the end of elements less than pivot
    // and k marks the start of elements greater than pivot
    // Elements from A[i+1:k] are equal to pivot

    return (i + 1, k)  // Return indices q and t
