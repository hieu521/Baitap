
# lis returns length of the longest increasing subsequence
# in arr of size n
def lis(lst):
    n = len(lst)
    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n
    prev = [0]*n
    for i in range(0, n):
        prev[i] = i
    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if lst[i] > lst[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
                prev[i] = j
    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0
    idx = 0
    # Pick maximum of all LIS values
    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]
            idx = i
    seq = [lst[idx]]
    while idx != prev[idx]:
        idx = prev[idx]
        seq.append(lst[idx])
    return (maximum, reversed(seq))
# end of lis function
# Driver program to test above function
lst = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
ans = lis(lst)
print ("Length of lis is", ans[0])
print ("The longest sequence is", ", ".join(str(x) for x in ans[1]))