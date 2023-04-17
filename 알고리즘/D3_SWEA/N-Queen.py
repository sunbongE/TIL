# 알고리즘 수행 과정을 정리하자면
# 위 첫 줄부터 퀸을 놓을 수 있는 위치에 두고 다음 칸으로 넘어간다.
# 다음 칸으로 넘어가면 어느 줄에 퀸을 둘 수 있는지 판단한다.


# 만약 가능하다면 넣고 불가능 하다면
# return 으로 재귀를빠져 나간다.
# 종료 조건: n == N
# n을 증가하는 부분은 퀸을 둘 수 있을 때 1증가하는 것 같다.
# n = 행번호 역할
# y  = 열번호 역할
def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    for y in range(N):
        if v1[y] == v2[n + y] == v3[n - y] == 0:
            v1[y] = v2[n + y] = v3[n - y] = 1
            dfs(n + 1)
            v1[y] = v2[n + y] = v3[n - y] = 0


for case in range(1, int(input()) + 1):
    N = int(input())
    ans = 0
    v1, v2, v3 = [[0] * (2 * N) for _ in range(3)]
    dfs(0)
    print(f"#{case} {ans}")
