# 인사성 밝은 곰곰이
import sys
sys.stdin = open('곰곰이.txt','r')
dic={}
cnt=0
for _ in range(int(input())):
    Input=input()
    if Input=="ENTER":
        for key,value in dic.items():
            if value==1:
                cnt+=1
        dic={}
    else:
        if Input not in dic:
            dic[Input]=1

for key,value in dic.items():
    if value==1:
        cnt+=1

print(cnt)