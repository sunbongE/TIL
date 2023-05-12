t = int(input())
for case in range(1, 1 + t):
    st_li = []
    result = ""
    for _ in range(5):
        st_li.append(input())
    for i in range(15):
        for j in range(5):
            if len(st_li[j]) - 1 < i:
                continue
            else:
                result += st_li[j][i]
    print(f"#{case} {result}")


# Aa0aPAf985Bz1EhCz2W3D1gkD6x
# Aa0aPAf985Bz1EhCz2W3D1gkD6x
