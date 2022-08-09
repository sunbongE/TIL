# 난쟁이 7명인데 2명 간첩들어옴 난쟁이 키 합은 100
import sys
sys.stdin = open('일곱난쟁이.txt','r')
nan = []
 
for _ in range(9):
    heigh = int(input())
    nan.append(heigh)
# print(nan)
for a in range(9):
    # print(nan[a])
    for b in range(a+1,9):
        # print(nan[a],nan[b])
        for c in range(b+1,9):
            for d in range(c+1,9):
                for e in range(d+1,9):
                    for f in range(e+1,9):
                        for g in range(f+1,9):
                            
                            v = [nan[a],nan[b],nan[c],nan[d],nan[e],nan[f],nan[g]]
                            # print(sum(v))
                            if sum(v) == 100:
                                ans = v
ans.sort()
for num in ans:
    print(num)
