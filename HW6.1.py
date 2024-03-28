RECURSIVE-TREE-INSERT(T, z)
    if T.root == NIL
        T.root = z
        z.p = NIL // Set parent of root as NIL
    else
        INSERT(NIL, T.root, z)

INSERT(p, x, z)
    if x == NIL
        z.p = p
        if p != NIL // Ensure p is not NIL before comparing keys
            if z.key < p.key
                p.left = z
            else
                p.right = z
    else if z.key < x.key
        INSERT(x, x.left, z)
    else
        INSERT(x, x.right, z)
