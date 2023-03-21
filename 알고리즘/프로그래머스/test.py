def solution(sizes):
    min_ = 0
    max_ = 0
    for s in sizes:
        big = max(s)
        small = min(s)

        if big > max_:
            max_ = big
        if small > min_:
            min_ = small

        # print(big, small)
    return min_ * max_


a = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
b = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
c = [[60, 50], [30, 70], [60, 30], [80, 40]]
# print(solution(a))
# print(solution(b))
print(solution(c))
