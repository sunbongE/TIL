def solution(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        print(idx , citation)
        if idx >= citation:
            # print(idx)
            return idx
    return len(citations)
solution([3, 0, 6, 1, 5])
    