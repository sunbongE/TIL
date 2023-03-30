import sys

input = sys.stdin.readline
dct_ground = {}

i_n, i_m, i_b = map(int, input().split())
for i_1 in range(i_n):  # 입력 받으면서 딕셔너리에 각 높이의 개수를 저장한다.
    mat = map(int, input().split())
    for i_2 in mat:
        dct_ground[i_2] = dct_ground.get(i_2, 0) + 1

# print(dct_ground)
ls_result = []

# 매트릭스 최소 높이에서 최대까지 순회
for ground_target in range(min(dct_ground.keys()), max(dct_ground.keys()) + 1):
    # print(ground_target)
    result_b = i_b  # 인벤토리에 있는 블럭 수 복제
    result_t = 0  # 걸리는 시간

    for ground_height, ground_cnt in dct_ground.items():  # 매트리스의 높이와 개수
        if ground_height > ground_target:  # 매트릭스가 현재 순회 높이보다 높다면
            result_t += (
                2 * (ground_height - ground_target) * ground_cnt
            )  # 시간: 2초*제거한 높이 * 같은 높이의 개수
            result_b += (
                ground_height - ground_target
            ) * ground_cnt  # 인벤토리: 제거한 높이 * 같은 높이 개수

        else:  # 매트릭스가 순회 높이보다 낮다면,
            result_t += (ground_target - ground_height) * ground_cnt  # 채우는데 걸리는 시간
            result_b -= (ground_target - ground_height) * ground_cnt  # 내 인벤토리에서 n개 사용

    if result_b >= 0:  # 인벤토리의 개수가 0보다 크다는 것은 정상적인 방법이라는 것
        ls_result.append((ground_target, result_t))
# print(ls_result)
result = min(ls_result, key=lambda x: (x[1], -x[0]))
print(result)
print(result[1], result[0])
