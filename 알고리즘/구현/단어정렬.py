N = int(input())
word_list = [[] for _ in range(20001)]

for _ in range(N):
    word = input()
    if word not in word_list[len(word)]:
        word_list[len(word)].append(word)

for words in word_list:
    for word in sorted(words):
        print(word)
