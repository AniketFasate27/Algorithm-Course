function TREE-INSERT(T, z)
1if x ≠ NIL then
    if z.key < x.key then
        TREE-INSERT-REC(x, x.left, z)
    else
        TREE-INSERT-REC(x, x.right, z)
    end if
end if
# In this block of code checks if the current node 'x' is not null. If 'x' is not null, 
#it means we are traversing down the tree to find the appropriate position for the new code 'z'.
# Depending on wether the key of 'z' is less than or greater than the key of the current node 'x', the recursion continues in the left or right subtree.

z.p = y
# after determining the appropriate subtree for insertion, the code sets the parent pointer of the new node 'z' to the current node 'y'.
# This line establishes the parent-child relationship between the current node 'y' and the newly inserted node 'z'.

if y == NIL then
    T.root = z
else if z.key < y.key then
    y.left = z
else
    y.right = z
end if

# This part of the code handles the actual insertion of the new node 'z' into the binary search tree.
# Its checks wether the aprent node 'y' is null. 
# If 'y' is null, it means that 'z' is the root of the tree. In this case, the root of the tree 'T.root' is set 'z'.
# If 'y' is not null, the code compare the key of 'z' with key of 'y'.
# #If the key of z is less than the key of 'y', then 'z' is assigned as the left child of 'y'. 
# Otherwise if the key of 'z' is greater than or equal to the key of 'y', then 'z' is assigned as the right child of the 'y' 