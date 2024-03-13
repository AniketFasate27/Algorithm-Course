function randomized_select(array, p, r, k):


 array: The array to be searched.
 p: The left index of the array to be searched.
 r: The right index of the array to be searched.
 k: The index of the kth smallest element to be found.
 q: The index of the pivot element after partitioning the array.
 x: The pivot element.
 i: The index that separates the elements smaller than or equal to the 
pivot element from the elements larger than the pivot element.
 if p == r:
    return array[p]
q = randomized_partition(array, p, r)
if k == q - p + 1:
return array[q]
elif k < q - p + 1:
return randomized_select(array, p, q - 1, k)
else:
return randomized_select(array, q + 1, r, k - (q - p + 1))
def randomized_partition(array, p, r):
i = random.randint(p, r)
array[i], array[r] = array[r], array[i]
return partition(array, p, r)
def partition(array, p, r):
x = array[r]
i = p - 1
for j in range(p, r):
if array[j] <= x:
i += 1
array[i], array[j] = array[j], array[i]
array[i + 1], array[r] = array[r], array[i + 1]
30)return i + 1
