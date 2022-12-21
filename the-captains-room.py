from collections import Counter

k = int(input())
lst = list(map(int,input().split()))
count = Counter(lst)
for num,cnt in count.items():
    if cnt == 1:
        print(num)
        