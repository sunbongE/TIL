import sys
import math

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    d = D * 2 + 1  # 분무기 하나당 물을 줄 수 있는 범위
    result = math.ceil(N / d)
    print(f"#{test_case} {result}")
