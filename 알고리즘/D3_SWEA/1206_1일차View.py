# 생각 정리..
# 우선 양쪽 끝의 두개가 0으로 들어오니까
# 탐색은 인덱스 2번부터
#
for _ in range(10):
    ans = 0
    N = int(input())
    buildings = list(map(int, input().split()))
    for i in range(2, N - 2):
        if (
            buildings[i] > buildings[i - 2]
            and buildings[i] > buildings[i - 1]
            and buildings[i] > buildings[i + 1]
            and buildings[i] > buildings[i + 2]
        ):
            target = max(
                buildings[i - 2], buildings[i - 1], buildings[i + 2], buildings[i + 1]
            )
            ans += buildings[i] - target
    print(f"#{_+1} {ans}")
