n = int(input())
n_student = set(input().split())
b = int(input())
b_student = set(input().split())

ans = n_student.union(b_student)
print(len(ans))