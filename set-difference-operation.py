n = int(input())
english = set(input().split())
m = int(input())
french = set(input().split())

ans = english.difference(french)
print(len(ans))