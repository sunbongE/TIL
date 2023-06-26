# 막대기

# 처음은 63막대기 하나가 이고
li = [64]
hap = 64
X = int(input())
# 모든 막대기 합이 x일때까지
while hap != X:
    target = li.pop(li.index(min(li))) // 2  # 가장 작은 것을 반으로
    if (sum(li) + target) >= X:
        li.append(target)
    else:
        li.append(target)
        li.append(target)
    hap = sum(li)
print(len(li))
