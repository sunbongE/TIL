import sys

input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    li.append(int(input()))

for i in sorted(li):
    print(i)
