#This line defines the PRINT_LCS function which taes the dyanmic programming table 'c', sequences 'x' and 'y' and the current indices 'i' and 'j'.
PRINT_LCS(c, x, y, i, j)
	if i = 0 || j = 0 #This line checks if either 'i' or 'j' is zero. If true, it meanss we have reached the end of one of the sequences, and the LCS has been completely prinmted. In such casses the function returns without printing anything.
		return 
	if x[i] = y[j] # Tihs line checks if the characters at positions 'i' in sequence 'x' and 'j' in sequence 'y' are equal. If true, it menas these characetrs are part of the LCS. Its then moves diagonally by recursively calling 'PRINT_LCS' on the previous position (i-1, j-1) and printsthe character x[i].
		PRINT_LCS(c, x, y, i-1, j-1)
		print x[i]
	elif c[i-1, j] >= c[i, j-1] # This linke checks if the value in the dyanamic programming table 'c' at position (i-1,j) is greater than or equal to the value positiion (i, j-1). if true it means that current chraacter x[i] is not part of the LCS, and it moves to the cell above (i-1,j) by recursively by calling 'PRINT_LCS'
		PRINT_LCS(c, x, y, i-1, j)
	else
		PRINT_LCS(c, x, y, i, j-1)