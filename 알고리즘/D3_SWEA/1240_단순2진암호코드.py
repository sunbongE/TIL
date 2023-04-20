dogam = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

for case in range(1, int(input()) + 1):
    ans = 0  # 답 0으로 초기화
    result_list = []
    N, M = map(int, input().split())
    amho = [input() for _ in range(N)]
    # print(amho)
    for ah_line in amho:
        if "1" in ah_line:
            for idx in range(len(ah_line) - 1, -1, -1):
                if ah_line[idx] == "1":
                    s_idx = idx - 55
                    e_idx = idx
                    break
            target = ah_line[s_idx : e_idx + 1]
            break
            # ah_line을 역 순회하면서 처음 1의 위치를 찾는다.
            # 그 위치로부터 [idx - 55] => 이게 암호의 시작 위치..
            # 이 위치 만큼 아래 과정으로 보내어 결과를 도출할 수 있다.
    # 10진수로 풀이
    for i in range(0, 55, 7):
        result_list.append(dogam[target[i : i + 7]])
    # 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.
    even = 0  # 짝수
    odd = 0  # 홀수
    for i in range(len(result_list)):
        if (i + 1) % 2 == 0:  # 짝수면
            even += result_list[i]
        else:
            odd += result_list[i]
    # print(even, odd)
    if (even + odd * 3) % 10 == 0:  # 10의 배수확인
        ans = even + odd

    print(f"#{case} {ans}")


# dct = {
#     "0001101": 0,
#     "0011001": 1,
#     "0010011": 2,
#     "0111101": 3,
#     "0100011": 4,
#     "0110001": 5,
#     "0101111": 6,
#     "0111011": 7,
#     "0110111": 8,
#     "0001011": 9,
# }


# def solve():
#     for st in arr:  # arr 순회
#         if "1" in st:  # 순회하는 문자열 리스트안에 1이 있다면\
#             e = len(st) - 1  # 마지막 인덱스 값
#             while st[e] == "0":
#                 e -= 1  # 리스트 마지막부터 앞으로 가면서 1을 찾는 코드
#             # 7개씩 암호 읽어오기
#             ans = []
#             for i in range(e - 55, e + 1, 7):
#                 # e-55: 암호코드 시작 인덱스 번호 찾음
#                 # e+1: 마지막 암호코드
#                 ans.append(dct[st[i : i + 7]])
#             # 정상인 암호라면 값 리턴, 아니면 0
#             if (sum(ans[0:8:2]) * 3 + sum(ans[1:8:2])) % 10 == 0:
#                 return sum(ans[0:8:2]) + sum(ans[1:8:2])
#             else:
#                 return 0


# for case in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]

#     ans = solve()
#     print(f"#{case} {ans}")
