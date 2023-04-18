# N극(빨강) = 1, S극(파랑) = 2
# 빨강은 아래로 떨어지고
# 파랑은 위로 올라간다.
# 그러니까 위에서부터 순회하려면 파란색을 찾고
# 이전 값이 빨강이면 교차한 것이다.
# 그러니 이전 값도 변수(prev)에 저장해둔다.
# 이때 cnt += 1한다.
# 반복을 전부 돌고나서 cnt를 출력하면 답이된다.

for case in range(1, 11):
    N = int(input())
    # 배열입력
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        prev = 0
        for j in range(N):
            if arr[j][i] != 0:
                if arr[j][i] == 2 and prev == 1:
                    # print(i, j)
                    cnt += 1
                prev = arr[j][i]
    print(f"#{case} {cnt}")
