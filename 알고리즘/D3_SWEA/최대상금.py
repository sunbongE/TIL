def dfs(n):
    global ans
    # 종료 조건
    if n == cnt:
        ans = max(ans, int("".join(num_li)))
        return
    for i in range(L - 1):
        for j in range(i + 1, L):
            # 변경
            num_li[i], num_li[j] = num_li[j], num_li[i]

            # 가지치기. 무의미한 반복 작업 제거
            # 현재 바뀐 값이 이전에 했던 결과와 같다면 안 할것
            check = int("".join(num_li)) * 10 + n
            # print(check)
            if check not in visited:
                dfs(n + 1)
                visited.append(check)

            # 변경 내용 복구
            num_li[i], num_li[j] = num_li[j], num_li[i]


for _ in range(int(input())):  # 테스트케이스만큼
    num, cnt = input().split()
    cnt = int(cnt)  # 바꿀 수 있는 횟수

    num_li = list(map(str, num))  # 리스트에 한글자씩 넣음
    visited = []
    L = len(num_li)
    ans = 0

    dfs(0)
    print(f"#{_+1} {ans}")
