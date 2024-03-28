PRINT-LCS(c, X, Y, m, n):
    // 's' is initialized to hold the LCS of size c[m,n]
    Let 's' be an array of size c[m,n]
    
    if c[m,n] == 0:
        print "No common subsequence."
        return

    // Index for the end of LCS array
    index = c[m,n] - 1
    
    i = m
    j = n
    
    // Construct LCS in 's'
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            s[index] = X[i-1]
            i = i - 1
            j = j - 1
            index = index - 1
        else if c[i-1][j] >= c[i][j-1]:
            i = i - 1
        else:
            j = j - 1
    
    // Print the LCS
    for k from 0 to c[m,n]-1:
        print(s[k])
