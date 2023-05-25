H, W = map(int, input().split())

H_list = list(map(int, input().split()))

# 최대값의 인덱스
maxH_idx = H_list.index(max(H_list))
ans = 0  # 답
now_H = 0
# 정방향
for i in range(maxH_idx):
    if H_list[i] > now_H:
        now_H = H_list[i]
        continue
    ans += now_H - H_list[i]
# 역방향
now_H = 0
for i in range(W - 1, maxH_idx - 1, -1):
    if H_list[i] > now_H:
        now_H = H_list[i]
        continue
    ans += now_H - H_list[i]
print(ans)
