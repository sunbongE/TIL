#한수
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면,그 수를 한수라고 한다.
#  등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
#  N이 주어졌을 때, 1보다 크거나 같고, 
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
n = int(input()) #110
cnt = 0
for a in range(1,n+1): # 1~110
    if a < 100: # 99까진 한수임
        cnt += 1 # cnt == 99
    else:
        
        if int(str(a)[1]) - int(str(a)[0]) == int((str(a)[2])) - int(str(a)[1]): 
            cnt += 1
print(cnt)