from collections import Counter
size = input()
lst = []
ans = []

for i in range(int(size)):
    lst.append(input())
    
counter = Counter(lst)
for word,count in counter.items():
    ans.append(count)
print(len(counter))
print(*ans)