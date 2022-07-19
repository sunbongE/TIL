# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
#1234


n = 123
result = 0 
while n:
    # print(n) #123
    result += n%10 # 123%10 = 3
    n //= 10    #123 // 10 = 12
print(result)
    
    
 


    
