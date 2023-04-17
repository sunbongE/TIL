# 제시되는 길이만큼의 문자가 회문인지를 판별한다.
# 결과는 회문의 개수이다.


def is_palindrome(word):  # 회문 검사 함수.
    if word == word[::-1]:
        return True
    return False


for case in range(1, 11):
    n = int(input())
    cnt = 0
    arr = [list(map(str, input())) for _ in range(8)]
    n_arr = [[] for _ in range(8)]
    for x in range(8):
        for y in range(8):
            n_arr[x].append(arr[y][x])

    for i in range(8):
        for j in range(8 - n + 1):
            w = arr[i][j : j + n]
            if is_palindrome(w):
                cnt += 1
            w = n_arr[i][j : j + n]
            if is_palindrome(w):
                cnt += 1
    print(f"#{case} {cnt}")
# -----------------------------------------------
for t in range(2):
    t = t + 1
    k = int(input())
    n_list = [list(input()) for _ in range(8)]
    n_dict = {}
    for y in range(8):  # 회전한 문자열을 기록하는 문법
        for x in range(8):
            if x not in n_dict:
                n_dict[x] = [n_list[y][x]]
            else:
                n_dict[x] += [n_list[y][x]]
    print(n_dict)
    cnt = 0
    for y in range(8):
        for x in range(8 - k + 1):
            if n_list[y][x : x + k] == n_list[y][x : x + k][::-1]:
                cnt += 1
            if n_dict[y][x : x + k] == n_dict[y][x : x + k][::-1]:
                cnt += 1
    print("#" + str(t), cnt)
