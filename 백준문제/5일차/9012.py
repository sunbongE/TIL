# 괄호
import sys
sys.stdin = open('9012.txt','r')

n = int(sys.stdin.readline())

for _ in range(n):
    vps = []
    w = sys.stdin.readline().strip()
    for i in w:
        if i == '(': # ( 면
            vps.append(i) # ( 추가하고
        elif i ==')': # ) 면서 vps가 비어있지 않다면
            if vps:
                vps.pop() # 뒤에 꺼 빼
            else: print('NO'); break#비어있으면 
    else:#뒤에꺼 빼면서 여기까지 왔고
        if not vps: print('YES') # vps비어있으면
        else: print('NO') # 아니면


