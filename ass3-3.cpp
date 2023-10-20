def partitionThreeWay(A, p, r): 
#  'A' is the array to be partitioned, 
# 'p' is the start index of subarray 
# 'r' is the end index of the subarray

    x = A[p]  # Here we will see the first element (pivot element) and assign to the x  
    q = p # pointers which will help us to track the elements
    t = r # liked above here we are assigned pointers
    i = p # defininf the index to tranverse the subarray
    while i <= t: # here we compare that 'i' is less than or equal to 't'
    #  if while loop is true these will run upto it will true
        if A[i] < x:  # These will run when A[i] is less than to x, iyt means we want to move this element to the "less than" section 
        so we swap it with the ekement at position 'q' an dthen increment both 'q' and 'i'. This action movies the element to the left partition.
            A[q]= A[i] 
            A[i] = A[q]
            q  =q + 1
            i = i + 1
        elif A[i] > x:
            A[i]  = A[t] 
            A[t] = A[i]
            t =  t - 1
        else:
            i = i + 1
    
    return q, t
# here we are returning the q and t these are the boundrie sof the equal partition, which contaains 
all the elements equal to the pivot lelement. 

