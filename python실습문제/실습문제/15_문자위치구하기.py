# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지\\


word = 'kiwi'
index_a = 0
for i in word:
    index_a += 1
    if i == 'a':
        print(index_a-1)
        break       
    # elif index_a == len(word):  
    #     print(-1)   
    else:
        index_a = -1             

# 반복문으로 단어 한글자를 지날 때 마다 변수에 1 더해주고 만약 a를 만나면 더한 변수의 값-1 을 출력 1을 빼는 이유는 인덱스가 0부터 시작했기 때문이다. 나는 0에 1씩 더했으니 빼는게 맞다.

# a를 못 찾으면 전체 길이의 값이 변수에 할당되니까  

# 변수와 len(변수)가 같으면 -1 출력