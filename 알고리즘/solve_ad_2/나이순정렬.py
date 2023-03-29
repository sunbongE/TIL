import sys

input = sys.stdin.readline
users = []
for _ in range(int(input())):
    users.append(list(input().split()))

users.sort(key=lambda x: int(x[0]))
for user in users:
    print(*user)
