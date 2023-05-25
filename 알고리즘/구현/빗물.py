ans = 0
# 입력 높이 넓이
H, W = map(int, input().split())
# 높이
H_list = list(map(int, input().split()))
# 가장 큰 값의 인덱스
maxH_idx = H_list.index(max(H_list))

# 가장 큰 값의 인덱스 양 옆으로
# 정방향
now_H = 0
for i in range(maxH_idx):
    if H_list[i] > now_H:
        now_H = H_list[i]
        continue
    ans += now_H - H_list[i]

# 역방향
now_H = 0
for j in range(W - 1, maxH_idx - 1, -1):
    if H_list[j] > now_H:
        now_H = H_list[j]
        continue
    ans += now_H - H_list[j]

print(ans)
# 다음 수가 나보다 크면 현재 높이값 변경. continue

# 최대 값을 갱신하면서 다음 수와 차이를 ans += result 더해나감
# 4 8
# 3 1 2 3 4 1 1 2
