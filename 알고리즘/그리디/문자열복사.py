ans = 0
word1 = input()
word2 = input()
idx = 0
L = len(word2)
while idx < L:
    temp = ""

    if word1.find(word2[idx:]) != -1:  # 있으면
        ans += 1
        break

    for j in range(idx, L):
        temp += word2[j]  # 문자를 하나씩 더해줌

        if word1.find(temp) == -1:  # 없으면
            ans += 1
            idx = j
            break
    # print(temp)
print(ans)
