t = int(input())
for case in range(1, t + 1):
    cnt = 0
    N = int(input())
    line = []
    for _ in range(N):
        # 전선입력
        line.append(list(map(int, input().split())))
    line.sort()
    # x보다 x2가 크고 y보다 y2가 작으면 점선이 생긴다.
    for i in range(N - 1):
        for j in range(i + 1, N):  # 내 다음부터
            if line[i][0] < line[j][0] and line[i][1] > line[j][1]:
                cnt += 1
    print(f"#{case} {cnt}")
