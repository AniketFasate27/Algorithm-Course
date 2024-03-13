// Initialize graph G as Figure 22.4
Create vertices u, v, w, x, y, z
Add vertices to G's vertex list 
Add edges (u, v), (u, x), (v, y), (w, y), (w, z), (x, v), (y, x), (z, z) to G

Call DFS(G):
   Mark all vertices as unvisited  
   For each vertex v:
      If v is unvisited:
         Call DFS-Visit(v)

DFS-Visit(v): 
   Mark v as visited
   For each neighbor w of v: 
      If w is unvisited:
         Call DFS-Visit(w)


// Initialize graph G as Figure 22.6
Create vertices q, r, s, t, u, v, w, x, y, z  
Add vertices to G's vertex list
Add edges (q, s), (q, t), (q, w), (r, u), (r, y), (s, v), (t, x), 
            (t, y), (u, y), (v, w), (w, s), (x, z), (y, q), (z, x)

Call DFS(G)  // Same DFS procedure