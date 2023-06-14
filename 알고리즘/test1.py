# 일단 for문으로 순회
# 시작은 2부터 l-2까지
# 양옆 2까지 확인하고 그 중 가장 큰 값을 찾아서
# 현재 내 값이랑 빼면
# 그 뺀 값을 ans += 값
# 답이된다.
for case in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in range(2, N - 2):
        # 좌우 2이상
        if (
            li[i] > li[i - 1]
            and li[i] > li[i - 2]
            and li[i] > li[i + 1]
            and li[i] > li[i + 2]
        ):
            target = max(li[i - 2], li[i - 1], li[i + 1], li[i + 2])
            ans += li[i] - target
    print(f"#{case} {ans}")
