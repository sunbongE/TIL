for case in range(1, 1 + int(input())):
    n = int(input())
    st = ""
    ans = []
    cnt = 0
    while cnt != n:  # 입력
        inp = input()
        st += inp
        cnt += inp.count(".")
        cnt += inp.count("!")
        cnt += inp.count("?")
    # 구분자로 나눠서 저장.
    t = [".", "?", "!"]
    li = []
    prev = 0
    for i in range(len(st)):
        cnt = 0
        if st[i] in "?!.":
            words = st[prev:i].strip().split()
            prev = i + 1
            for word in words:
                if (  # 첫글자가 대문자고 나머지는 소문자고 전부 알파벳인거
                    word[0].isupper()
                    and word.isalpha()
                    and word[1:].islower()
                    or len(word) == 1  # 길이 1인데 이름인거
                    and word.isupper()
                ):
                    cnt += 1
            ans.append(cnt)
    print(f"#{case}", end=" ")
    print(*ans)
