RIGHT-ROTATE(T,x):
    y = x.left 
    x.left = y.right 
    if ( y.right != NIL ): 
        y.right.p = x 
    y.p = x.p 
    if ( x.p == T.nil ): 
        T.root = y 
    elseif ( x == x.p.left ): 
        x.p.left = y 
    else: 
        x.p.right = y 
    y.right = x 
    x.p = y 