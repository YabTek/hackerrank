def isSuperset(setA):
    n = int(input())
    for _ in range(n):
        N_sets = set(map(int,input().split()))
        if not A.issuperset(N_sets):
            return False
    return True

A = set(map(int,input().split()))
print(isSuperset(A))    