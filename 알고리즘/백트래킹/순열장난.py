from sys import exit

s = input()
l = len(s)  # 입력 길이
N = l if l < 10 else (l - 9) // 2 + 9  # 순열의 개수 구하기.
D = [0] * (N + 1)  # 방문 표시.


def DFS(idx, path):
    if idx >= l and sum(D[1:]) == N:  # 순열 개수만큼 방문된경우
        print(*path)
        exit(0)
    for i in range(1, 3):  # 1~2까지 1의 자리 2의 자리 조회
        if idx + i <= l:  # 인덱스 범위내
            n = s[idx : idx + i]
            if n[0] != 0:  # 0이 아니면
                n = int(n)
                if n <= N and not D[n]:  # 범위 내, 방문안됨
                    D[n] = 1
                    DFS(idx + i, path + [n])
                    D[n] = 0


DFS(0, [])
