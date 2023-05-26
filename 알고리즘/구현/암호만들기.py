# 116ms
from itertools import combinations


def is_valid(word):
    cnt = 0
    check1 = ["a", "e", "i", "o", "u"]
    cnt = len(set(word) - set(check1))
    for w in word:
        if w in check1:  # 모음이 있음
            if cnt >= 2:  # 모음을 제외한 길이가 2이상
                result.append("".join(sorted(word)))
                return
    return False


L, C = map(int, input().split())

alpa = list(input().split())
alpa.sort()
# print(alpa)
result = []
for com in combinations(alpa, L):
    is_valid(com)
result.sort()

for ans in result:
    print(ans)


# ===백트래킹 풀이=====================144ms=====================================
def valid(word):
    L = len(word)
    cnt = 0
    for w in word:
        if w in "aeiou":
            cnt += 1
    if L - cnt > 1 and cnt != 0:
        return True
    else:
        return False


def dfs(n, temp):
    if C == n:
        if len(temp) == L:
            alpa = "".join(temp)
            if alpa not in ans:
                ans.append(alpa)
        return
    dfs(n + 1, temp + [alpas[n]])
    dfs(n + 1, temp)


ans = []
L, C = map(int, input().split())
alpas = list(map(str, input().split()))
alpas.sort()
dfs(0, [])
for answer in sorted(ans):  # 여기 모인 예비 답안 중 최소 하나의 모음과 두개의 자음이 있어야한다.
    if valid(answer):
        print(answer)
