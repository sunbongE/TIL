import sys

input = sys.stdin.readline

N = int(input())

n_list = list(map(int, input().split()))
presum = [n_list[0]]

for i in range(1, N):
    presum.append(presum[-1] + n_list[i])


M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print(presum[b - 1])
    else:
        print(presum[b - 1] - presum[a - 2])
