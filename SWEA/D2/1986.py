n = int(input()) #2

for i in range(1,n+1):
    val = int(input()) # 6
    space_1 = 0
    for j in range(1,val+1): # 1~6 까지
        if j % 2 == 0:
            space_1 -= j
        else:
            space_1 += j

    print(f'#{i}',space_1)
