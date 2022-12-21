happiness = 0
n,m = map(int,input().split())
lst = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

for num in lst:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1
        
print(happiness)
