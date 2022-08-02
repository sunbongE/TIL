#저항문제
import sys
sys.stdin = open('저항.txt','r')
re = []
dic={
    'black' : (0,1),
    'brown' : (1,10),
    'red' : (2,100),
    'orange' : (3,1000),
    'yellow' : (4,10000),
    'green' : (5,100000),
    'blue' : (6,1000000),
    'violet' : (7,10000000),
    'grey' : (8,100000000),
    'white' : (9,1000000000)

}

for i in range(3):
    color = sys.stdin.readline().strip()
    re.append(dic[color])

result = int(str(re[0][0]) + str(re[1][0])) * int(re[2][1])
print(result)

 