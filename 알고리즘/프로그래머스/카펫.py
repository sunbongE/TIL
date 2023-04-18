def solution(brown, yellow):
    # brown + yellow 의 약수를 구한다.
    # 약수 중 차이가 가장 작은 한쌍을 찾는다.
    # 한쌍에서 내림차순정렬한다.

    ans = []
    temp = []
    target = brown + yellow
    # 약수어캐찾니
    # 1부터 현재 수까지 나눠서 떨어지는거 찾으면 약수였던 기요쿠가..
    for n in range(2, target):
        if target % n == 0:
            temp.append(n)
    # 가운데꺼 뽑으면 되는듯..
    # 길이를 반으로 =>
    # print(temp)
    if len(temp) % 2 == 0:
        mid = len(temp) // 2
        i = 1
        x = temp[mid]
        y = temp[mid - 1]
        if (x - 2) * (y - 2) == yellow:
            ans = [x, y]
        else:
            while 1:
                if (x - 2) * (y - 2) == yellow:
                    ans = [x, y]
                    break
                x = temp[mid + i]
                y = temp[mid - 1 - i]
                i += 1

    elif len(temp) % 2 == 1:
        mid = len(temp) // 2
        ans = [temp[mid], temp[mid]]

    return ans


# print(solution(12, 3))
# print(solution(12, 4))
# print(solution(8, 1))
# print(solution(14, 6))
# print(solution(14, 4))
print(solution(18, 6))

111111
100001
111111
