def atMostSum(arr, n, k):
    _sum = 0
    cnt = 0
    maxcnt = 0
    for i in range(n):
        if ((_sum + arr[i]) <= k):
            _sum += arr[i]
            cnt += 1
        elif(sum != 0):
            _sum = _sum - arr[i - cnt] + arr[i]
        maxcnt = max(cnt, maxcnt)
    return maxcnt
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 8
print(atMostSum(arr, n, k))