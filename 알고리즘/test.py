def solution(dots, lines):
    lines.sort()
    answer = 0
    new = []
    L = len(dots)
    if L % 2 == 0:  # 짝수개
        for i in range(0, L, 2):
            new.append(dots[i + 1] - dots[i])

    else:  # 홀수개
        new.append(dots[0])
        if L > 2:
            for i in range(1, L, 2):
                new.append(dots[i + 1] - dots[i])
        else:
            pass
    print(new)
    check = 0
    for n in new:
        for i in range(check, len(lines)):
            check += 1
            if n <= lines[i]:
                answer += 1
                break

    return answer


print(solution([1, 5, 8], [1, 3, 4, 6]))
print(solution([1, 3, 4, 6, 7, 10], [2, 2, 2, 2]))
