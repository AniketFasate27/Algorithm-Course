BOTTOM-UP-FIB(n):
    if n <= 1: 
        return n 

    // Initialize the array with n+1 elements to store computed values
    Let r[0..n] be a new array
    
    // Base cases
    r[0] = 0 
    r[1] = 1 
    
    // Compute Fibonacci numbers from 2 to n
    for i from 2 to n:
        r[i] = r[i-1] + r[i-2]
    
    // Return the nth Fibonacci number
    return r[n]
