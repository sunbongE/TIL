# 최대 높이를 기준으로 양옆에서 최대 높이 전까지 이동하면서 현재의 최대 높이를 계속 더해준다.
N = int(input())
h_list = [0] * 1001
max_H = 0
max_L = 0
for idx in range(N):
    L, H = list(map(int, input().split()))
    if H > max_H:  # 최대값과 인덱스 찾는거
        max_H = H
        max_L = L
    # hlist에 기록해야함.
    h_list[L] = H
cur = 0
ans = max_H  # 최대 높이를 답에 포함하고 시작한다.
for i in range(max_L):  # 정방향으로 처음부터 중간지점까지 이동.
    cur = max(cur, h_list[i])  # 현재 가장 큰 높이를 더해줌
    ans += cur

# 역방향으로 순회
r_cur = 0
for i in range(1000, max_L, -1):
    r_cur = max(r_cur, h_list[i])
    ans += r_cur
print(ans)
