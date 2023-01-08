st = input()


cnt = 0 
for i in range(len(st)-1):
    if st[i] != st[i+1]:
        # print('현재'+st[i], '다음' + st[i+1])
        cnt += 1

print((cnt+1)//2)