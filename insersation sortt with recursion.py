def recursiv_insersation(arr, n):
    # array with the size of 1 or 0 is sorted 
    if n <= 1: # if array is already is sorted 
        return 
    # Now we have to sort the first n-1 items
    recursiv_insersation(arr, n-1)

    # We have to insert the nth item in the sorted part
    key = arr[n-1]
    j = n-2
    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -=1
        arr[j + 1] = key
        





    