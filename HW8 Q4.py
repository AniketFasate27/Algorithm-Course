let Adj'[1..|V|] be a new adjacency list of the transposed G^T
for each vertex u ∈ G.V
    for each vertex v ∈ Adj[u]
        INSERT(Adj'[v], u)