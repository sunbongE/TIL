from pprint import pprint


def solution(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]  # dp[i][j]: i부터 j까지의 부분문자열이 팰린드롬인지 여부
    answer = 1  # 팰린드롬 길이의 최솟값은 1

    # 길이가 1인 부분문자열은 모두 팰린드롬이므로 True로 초기화
    for i in range(n):
        dp[i][i] = 1

    # 길이가 2인 부분문자열의 팰린드롬 여부를 판단하여 dp 배열 업데이트
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
            answer = 2

    # 길이가 3 이상인 부분문자열의 팰린드롬 여부를 판단하여 dp 배열 업데이트
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1
                answer = length
    pprint(dp)
    return answer


print(solution("abacde"))
print(solution("abcdcba"))
