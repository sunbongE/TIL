def solution(clothes):
    answer = 1
    dtn = dict()

    for i, k in clothes:
        dtn[k] = dtn.get(k, 0) + 1
    for k in dtn:
        # print(dtn[k])
        answer *= dtn[k] + 1
        # print(answer)
    return answer - 1


solution(
    [
        ["yellow_hat", "headgear"],
        ["blue_sunglasses", "eyewear"],
        ["green_turban", "headgear"],
    ]
)
