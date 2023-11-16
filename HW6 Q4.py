
function RIGHT-ROTATE(tree,x):

    y = x.left 

    x.left = y.right 

    if y.right =! NIL
        y.right.parent = x

# St the aprent of y to be the same as the parent of x. This updates 
# the parent pointer of y to point to the same node that was the parent of x.
    y.parent = x.parent

# if x was the root of the tree means its parents is NIL, update the root of the tree to be y. 
    if x.parent = NIL
        tree.root = y

#if x was the right 






# here we can write the pseudo code for the RIGHT-ROTATE
# here we declearing the function in which we are passing two parameters 
# tree which is the binary search tree and x the node around the ehich the rotation is performed
 
function  RIGHT-ROTATE(tree, x)

# set y to the left child of x . This is the node that will replace the x as the new root after the rotation.
    y = x.left 
 
# update the left child of x to the right child of y. This moves takes the right subtree 
# of y and attches it as the left subtree of x.
    x.left = y.right  


#if y.right is not a null node is NIL, update the parent pointer of y.right to point 
# to x. This is important for maintaining the parent-child relationships.
    if y.right =! NIL
        y.right.parent = x  

# set the parent of y to be the same as the parent of x. This updates the 
# parent pointer of y to point to the same node that was the parent of x.

    y.parent = x.parent  
# If x was the root of the tree its parent is NIL, update the root of the tree to be y.
   
    if x.parent = NIL
        tree.root = y  // If x was the root, update the root of the tree
# If 'x' was the root of the entire taht is it hass no parent, this line updates the root of the tree.
# to be y. This signifies the chnage in the overall tree structure. 

    else if x = x.parent.right
        x.parent.right = y  // If x was a right child, update the right child of x's parent
#If 'x' was the right child of its parent, this line updates the right child pointer of 'x' is parent to point to 'y'  
    else
        x.parent.left = y   // If x was a left child, update the left child of x's parent

# These lines complete the right rotation operation. 'x' is placed on the right of 'y' and the aprent pointer of 'x' 
# is updated to point to 'y'. After this, the binary tree is appropriately modified, and 'y' become the new root of the subtree.
    y.right = x  // Put x on y's right
    x.parent = y  // Update the parent pointer of x to y


