# 제곱수의 합
n = int(input())
m = int(n**0.5)  # 제곱근
# print(m)
dp = [a for a in range(n + 1)]  # 초기 데이터

for i in range(2, m + 1):  # 2부터 제곱근까지
    for j in range(i * i, n + 1):  # 변경이 되는 범위부터 순회
        dp[j] = min(dp[j], dp[j - i * i] + 1)  # 현재값과 제곱수를 뺀 위치 값에 1 더한 값 중 작은거.
        # print(dp,i,j)
print(dp[n])
