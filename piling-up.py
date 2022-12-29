test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    lst = list(map(int, input().split()))
    m = len(lst)
    temp = max(lst)
    if (temp > lst[m-1]) and (lst[0] < temp):
        print('No')
    else:
        print('Yes')
