function Fibonnacci(n):
# Tihs line declarees a fucntional named 'fibionacci' taht takes an integer parameter 'n' 
# representing the index of the Fibonacci number to be completed.
    if n <= 1: # This line is a base case ckeck.If 'n' is 0 or 1, the functional retruns 'n' since the fibonnaci numbers for indices 0 and 1 are 0 and 1 respectively. 
        return n 
# This line initializes an array 'fib' of size 'n+1' to store intermediate results. The arrayt is used to store teh Fibonnacci numbers from 0 to n.
    lets fib[0....n] be a new array
    # These lines set the initaila values of the fibonacci sequence. 'fib[0]' is set to 0. and 'fib[1]' is set to 1, as these are the base cases. 
    fib[0] = 0 
    fib[1] = 1
    # This loop iterates for 2 ot n, calculating each fibonacci number iteratively by summing the two preceding fibonacci numbers. The values are stored in the 'fib' array.
    for i = 2 to n:
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]
    # Here this line returns the comutedfibonacci number atinex 'n'. The result is obtained by the dynamic programming approach.
    

