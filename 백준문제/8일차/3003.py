# 킹, 퀸, 룩, 비숍, 나이트, 폰
# 흰 피스 개수가 바르지 않다
# 체스는 총 16개의 피스를 사용하며,
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.
# 몇개를 더하거나 빼야 올바른 세트인지 알아내는 문제
import sys
sys.stdin = open('체스.txt','r')
chess = [1, 1, 2, 2, 2, 8]
inp = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i] - inp[i], end=' ')    