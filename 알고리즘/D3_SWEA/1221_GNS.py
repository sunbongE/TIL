li = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for __ in range(1, 1 + int(input())):
    case, n = input().split()
    inp = list(input().split())
    result = []

    for target in li:
        cnt = 0
        cnt = inp.count(target)
        if cnt:
            for _ in range(cnt):
                result.append(target)

    print(case)
    print(*result)
