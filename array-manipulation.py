def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for start,end,value in queries:
        arr[start-1] += value
        arr[end] -= value
    max_ = 0
          
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
        max_ = max(max_,arr[i])
        
    return max_