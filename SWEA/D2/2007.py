# 몇번 반복되는지 알아내는거
from re import A
import sys
sys.stdin = open('2007.txt')
for case in range(int(input())):
    st = input()    

    is_word = ''
    for s in st:

        if len(is_word) > 1 and is_word[0] == s:
            T = len(is_word)
            if st[:T] == st[T:T*2]:
                # print(st[:T], st[T:T*2])
                
                ans = len(is_word)
                break
            is_word += s

        else:
            is_word += s
    print(f'#{case+1} {ans}')

    
# -------------------------------------------------
# T = int(input())
# for tc in range(1, T+1):
    
#     text = input()
#     patten =[]
#     next_patten=[]
#     ans = 0
#     for i in range(11):					# 마디의 최대 길이가 10이므로 range(11)
#         patten = text[:i]				# patten리스트에 패턴 입력
#         next_patten = text[i:i*2]		# 다음 패턴 입력
#         print(patten)
#         print(next_patten)
#         if i!=0 and patten == next_patten :	# 다음 패턴과 이번 패턴이 같은경우
#             ans = len(patten)			# 길이 출력
#             break
    # print('#{} {}'.format(tc, ans))


# 음
# 한 글자씩 저장하다가 is_word의 첫 글자와 같은 글자가 나오면 
# 음... 같은 글이 나오면 st에서 슬라이싱을 하는데 길이는 
# is_word의 만큼 해서 같다면 단어인건가#


