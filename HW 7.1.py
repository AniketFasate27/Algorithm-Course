Function Modified-CUT-ROD(p, n, c):
# p = an array representing the the prices for each rod length
# n = the total of the rod
# c = the fixed cost for each cut.
    let r[0....n] be a new array
# This line initializes a new array 'r' of length 'n+1' to store the maximum revenue 
# for rods of different lengths. The array is zero-indexed, so it goes from 'r[0]' to 'r[n]'
    r[0] = 0 # This line sets the base for a rod of length 0. The maximum revenue for a rod of lenth 0 is always 0.
    for j = 1 to n # here line starts a lopp that iterates through rod lengths from 1 to 'n'. The variable 'j' represents the current rod length.
        q = p[j] # This  line initializes a variable 'q' with the price of the current rod length 'p[j]'. this is the initial assumption that not cutting the rod at all might be the optional solution.
        for i = 1 to j-1 # Here we are starts an inner loop that iterates through possible cuts for the current rod length. The variable 'i' represenyts a possible cut point, ranging from 1 to 'j-1'.
            q = max(q, p[i] + r[j-i] -c) # here we are updates the variable 'q' by considering the maximum revenue obtained by either not cutting the rod at all whic is current value of q or making a cut at position 'i' 
# and adding the revenue form the cut piece p[i] and the revenue from the remianing rod length r[j-1] while subtracting the fixed cost 'c'.
        r[j] = q # this line update the array 'r' ata index 'j' with the maximum revenue 'q' obtained for the rod of length 'j'.
    return r[n] # This line updates the maximum reveune for a rod length 'n', which is stored in 'r[n]'. The function 
# calculates and returns the optimal revenue considering the fixed cost of making cuts. 

