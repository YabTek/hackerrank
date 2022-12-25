from collections import defaultdict

A = defaultdict(list)
n,m = map(int,input().split())
idx = 1

for _ in range(n):
    A[input()].append(idx)
    idx += 1
for _ in range(m):
    B = input()
    if B in A:
        print(*A[B])
    else:
        print(-1)
