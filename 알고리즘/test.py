#  슬라이딩 윈도우
N, K = map(int, input().split())
temp_list = list(map(int, input().split()))

part_sum = sum(temp_list[:K])
answer = part_sum

for i in range(N - K):
    part_sum += temp_list[i + K] - temp_list[i]
    # print(temp_list[i + K], temp_list[i], part_sum)
    if answer < part_sum:
        answer = part_sum

print(answer)
