import sys
import math

n, k = map(int, sys.stdin.readline().split())
answer = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
print(answer)
