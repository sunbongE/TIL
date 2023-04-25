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
