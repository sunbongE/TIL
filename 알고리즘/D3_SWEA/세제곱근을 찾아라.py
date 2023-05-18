# 5688. 세제곱근을 찾아라
for case in range(1, 1 + int(input())):
    N = int(input())
    ans = -1
    s, e = 1, N
    # 2분 탐색
    while s <= e:  # 시작과 끝이 같거나 시작이 더 커지면 종료
        mid = (s + e) // 2
        if mid**3 == N:  # 목표치
            ans = mid
            break
        if mid**3 > N:  # 목표 값보다 크면, 끝값을 바꿔준다.
            e = mid - 1
        else:
            s = mid + 1
    print(f"#{case} {ans}")
