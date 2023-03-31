import sys

input = sys.stdin.readline

# 내 풀이
N, M = map(int, input().split())
dogam = {}
for i in range(1, N + 1):
    P = input().strip()
    i = str(i)
    dogam[P] = i
    dogam[i] = P


for _ in range(M):
    pocketmon = input().rstrip()
    print(dogam[pocketmon])
print(dogam)

# GPT 풀이
N, M = map(int, input().split())
dogam = {}
for i in range(1, N + 1):
    P = input().strip()
    i = str(i)
    dogam[P] = i
    dogam[i] = P

while M:
    pocketmon = input().rstrip()
    print(dogam[pocketmon])
    M -= 1
