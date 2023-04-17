# # 우선 입력 받은 상태에서 2중 for 문으로 순회한다.

# # i, L-1
# # i+1,L

# # 내림 차순 정렬을 해본다.
# # arr[i] == k : cnt +=1
# # 이거 아니면 temp = arr[i] temp변경하고


# # temp += arr[i+1] 해나간다.
# # 여기에 if문 또 적용
# # if temp == k : cnt+=1   #
# # elif temp > k: break # 더해 나간 것이 타겟 값ㅂ다 크면 더이상 안본다.


# GPT- DP 풀이
def count_subset_sum(numbers, target):
    n = len(numbers)
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # dp[i][j]는 numbers[0]~numbers[i-1] 중에서 j를 만들 수 있는 부분집합의 개수
    for i in range(n + 1):
        dp[i][0] = 1
    # print(dp)

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if numbers[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - numbers[i - 1]]
    print(dp)
    return dp[n][target]


t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    count = count_subset_sum(numbers, k)
    print(f"#{i} {count}")


# 빽트래킹 풀이.
def dfs(n, sm):
    global cnt
    if K < sm:
        return
    if n == N:
        if sm == K:
            cnt += 1
        return

    dfs(n + 1, sm + nums[n])  # 현재 위치 수를 사용한 경우
    dfs(n + 1, sm)  # 사용하지 않은 경우


for case in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    cnt = 0

    nums = list(map(int, input().split()))

    dfs(0, 0)
    print(f"#{case} {cnt}")
