# 4466 최대성적표만들기.
for case in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    score.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += score[i]

    print(f"#{case} {ans}")
