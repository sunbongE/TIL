for case in range(1, 1 + int(input())):
    result = [[] for _ in range(5)]
    st = input()
    for i in range(len(st)):
        result[0] += ["..#."]
        result[1] += [".#.#"]
        result[2] += ["#." + st[i] + "."]
        result[3] += [".#.#"]
        result[4] += ["..#."]
    # 겹치는 부분을 마지막에 삽입
    result[0] += ["."]
    result[1] += ["."]
    result[2] += ["#"]
    result[3] += ["."]
    result[4] += ["."]
    # print(result)
    for re in result:
        print("".join(re))  # 공백없이 문자열로 만들어서 출력.
