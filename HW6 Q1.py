#it is function in which we are passing two arguments BST T and 
# T which is new node that we have to insert in the tree. 
function tree_insert(T, key): 
# This line checks that BST is empty or not. 
# If BST is empty then we are putting key as the the root node. 
if T.root is NIL:
    T. root = key
# If not then we will placed the key in BST using recursive medthod
else: 
    insert(NIL, T.root, key)

#this lins declares the procedure insert, which takes three arguments a parent node p, a node x 
# and a new node key to be inserted into the tree 

function insert(p,x,key):
# This lines checks if the node x is NIL. If it is then the new node 
# key is inserted as a child of the parent node p. The child position 
#of the new node is determined by comparing its key to the key of the parent nnode.

if x is NIL :
    key.p = p 
    if z.key < p.key:
        p.left = key
    else 
        p.right = key

# If not then, the new node key is inserted inot the subtree of the node x
# that corresoonds to its key. This is done by recursively calling the INSERT 
#procedure with the node x and the appropriate subtree arguments.


