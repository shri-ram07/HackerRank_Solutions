def miniMaxSum(arr):
    minSum = 10000000000000000000
    maxSum = 0
    li = list(itertools.combinations(arr,4))
    for x in li:
        a,b,c,d = x
        sum = a+b+c+d
        if sum>maxSum:
            maxSum = sum
        if sum<minSum:
            minSum = sum
    print(minSum , maxSum)