MEMOIZED-CUT-ROD-AUX(p, n, r):
 if r[n] >= 0: 
 return r[n] 
 if n == 0: 
 q = 0 
 else q = -inf 
 for i = 1 to n: 
 q = max {q, p[i] +MEMOIZED-CUT-ROD-AUX(p, n-i, r) − (𝑖 == 𝑛 ? 0: 𝑐)}
 r[n] = q 
 return q 