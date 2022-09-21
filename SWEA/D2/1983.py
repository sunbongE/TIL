import sys
sys.stdin = open('1983.txt','r')

G = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


for case in range(int(input())):
    n,target = input().split()
    n = int(n)
    target = int(target)-1
    rank = []
    for _ in range(n):
        meq = list(map(int, input().split()))
        m = meq[0]
        e = meq[1]
        q = meq[2]
        total = round((m * 0.35) + (e * 0.45) + (q * 0.2),3)
        rank.append(total)
    target_v = rank[target]
    # print(target_v)
    rank.sort(reverse=True)
    ans = G[(rank.index(target_v))//(n//10)]
    
    # print(target_v)
    print(f'#{case+1} {ans}')
    # print(f'index:{rank.index(target_v)}')
    

    # 음 20명이면 2명씩 인덱스를 가져야함 
    # n0명이면 n명씩 
    # 12 // 2 = 6#