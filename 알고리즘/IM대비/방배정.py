# 방배정
# 남여 딕셔너리를 만들어서 각 학년의 개수를 기록하고
# 순회하면서 K를 넘는 학년이 있으면 학년//K를 ans에 더한다.
# 아니면 ans +=1 한다.
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
W_dic = dict()
M_dic = dict()
for _ in range(N):
    s, grade = map(int, input().split())

    if s:  # 남
        M_dic[str(grade)] = M_dic.get(str(grade), 0) + 1
    else:
        W_dic[str(grade)] = W_dic.get(str(grade), 0) + 1

ans = 0
for v in W_dic.values():
    if v > K:
        if v % K == 0:
            ans += v // K
        else:
            ans += v // K + 1
    else:
        ans += 1
for v in M_dic.values():
    if v > K:
        if v % K == 0:
            ans += v // K
        else:
            ans += v // K + 1
    else:
        ans += 1
print(ans)
# print(W_dic, M_dic)
