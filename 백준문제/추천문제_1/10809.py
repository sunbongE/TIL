# 알파벳 찾기
word = input() # baekjoon

# li = [-1] * 26

# for w in word:
#     ord_w = int(ord(w)) - 97  # a == 0, b == 1  ~~~
#     # print(ord_w)
#     for i in range(len(li)): # 0~ 25 반복
# # 첫번째 나오는 값의 자리에 1 증가 해줌 
        
#         if ord_w == i:
#             li[i] = word.index(w) 

# for i in li:
#     print(i, end = ' ')
            
l = list(range(97,123))
for i in l: #97~123까지 순회
    print(word.find(chr(i)),end =' ') 
    #find가 없으면 -1을 반환하는 성질을 이용해 풀이함
    