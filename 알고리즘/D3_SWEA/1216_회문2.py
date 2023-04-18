# 회문 2
# 100x100
# 가로, 세로 비교

# 음...
# 2중 for문으로 하나씩 돌면서
# li[i] == li[j]이게 같으면 팰린드롬인지 확인하는 함수호출
# 만약 맞다면 멈추는 식으로
# 그렇다면 가장 긴 문자열이 답이니까 큰수부터 점점작아지게 반복한다.
# li[i] == li[len(li)-j]


def is_palindrom(word):
    if word == word[::-1]:
        return True
    return False


for case in range(1, 11):
    cs = int(input())
    li = [list(map(str, input())) for _ in range(100)]
    ans = 0
    n_li = {}
    # 세로 만들기...
    for x in range(100):
        for y in range(100):
            if y not in n_li:
                n_li[y] = [li[x][y]]
            else:
                n_li[y] += [li[x][y]]
    # print(n_li)
    # 가로
    for ii in range(100):
        for i in range(100):
            for j in range(100 - 1, i, -1):
                # print(li[ii][i], li[ii][j])
                if li[ii][i] == li[ii][j]:
                    if is_palindrom("".join(li[ii][i : j + 1])):
                        # print("".join(li[ii][i : j + 1]))
                        ans = max(ans, len(li[ii][i : j + 1]))
                if n_li[ii][i] == n_li[ii][j]:
                    if is_palindrom("".join(n_li[ii][i : j + 1])):
                        ans = max(ans, len(n_li[ii][i : j + 1]))

    print(f"#{case} {ans}")


# ---------간단하지만 비효율적-------------------
def is_pal(arr, leng):
    for lst in arr:
        for i in range(N - leng + 1):
            if lst[i : i + leng] == lst[i : i + leng][::-1]:
                return True
    return False


for case in range(1, 11):
    cs = int(input())
    N = 100
    arr1 = [input() for _ in range(100)]
    arr2 = ["".join(x) for x in zip(*arr1)]  # 세로

    for leng in range(N, 1, -1):
        if is_pal(arr1, leng) or is_pal(arr2, leng):
            break

    print(f"#{case} {leng}")

# -----------------효율적----------------------


def is_pal_idx(arr, leng):
    for lst in arr:
        for i in range(N - leng + 1):
            for j in range(leng // 2):
                if lst[i + j] != lst[i + leng - 1 - j]:
                    break
            else:
                return True
    return False


for case in range(1, 11):
    cs = int(input())
    N = 100
    arr1 = [input() for _ in range(100)]
    arr2 = ["".join(x) for x in zip(*arr1)]  # 세로

    for leng in range(N, 1, -1):
        if is_pal_idx(arr1, leng) or is_pal_idx(arr2, leng):
            break

    print(f"#{case} {leng}")
