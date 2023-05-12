for case in range(1, int(input()) + 1):
    st = input()
    for s in st:
        if s in "aeiou":
            st = st.replace(s, "")
    print(f"#{case} {st}")
