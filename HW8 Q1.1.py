DYNAMIC-ACTIVITY-SELECTOR(s, f, n)
#This loine defines the main function "Dynamic activity selector" which take theree parameters  S which starttime and f which ius finish time and n which is the number of activities.
    let c[0..n + 1, 0..n + 1] and act[0..n + 1, 0..n + 1] be new tables
    #This line declares two tables c and act to store the solution to problems Tha tables have dimensions from 0 to n+1.
    for i = 0 to n
        c[i, i] = 0
        c[i, i + 1] = 0
    c[n + 1, n + 1] = 0
# These lines initilize the base casses of the dynamic programming table. For single activities, the maximum size subset is 0, so c[i,i] and c[i, i+1] are set 0.
    for l = 2 to n + 1
        for i = 0 to n - l + 1
            j = i + l
            c[i, j] = 0
            k = j - 1
# This lines iterates over the sbproblems of increasing lengths l. The nested loopconsiders different partitions of activities i to j withing the subproblems.
            while f[i] < f[k]
# This line starts a while loop that iterates as long as the finish time of the current activity F[i] is less than the finish time of the previous activity. 
                if f[i] ≤ s[k] and f[k] ≤ s[j] and c[i, k] + c[k, j] + 1 > c[i, j]
                    c[i, j] = c[i, k] + c[k, j] + 1
                    act[i, j] = k
                k = k - 1
# Thses lines checks if adding the current activity to the subset results in a larger size, considerig compatibility constratints. if so, it updates the dynaamic programming tables c and act table. This lines decrements the k to continue checking the previous activities,
    print "A maximum size set of mutually compatible activities has size" c[0, n + 1]
    print "The set contains"
    PRINT-ACTIVITIES(c, act, 0, n + 1)
#Thses lines print the maximum size set of mutually compatible activities and then call the print_activities function to print the actiual activities.
    PRINT-ACTIVITIES(c, act, i, j)
    if c[i, j] > 0
        k = act[i, j]
        print k
        PRINT-ACTIVITIES(c, act, i, k)
        PRINT-ACTIVITIES(c, act, k, j)
# These lines dedine the PRINT-ACTIVITIRS function a recursive function that prints the acriviries based on the information stored in the act table. It backtracks fro the last selected activity to the first printing each activity in reverse order.
