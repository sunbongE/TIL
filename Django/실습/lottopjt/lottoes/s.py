import random
ss = [3, 11, 15, 29, 35, 44]
bonus = 10
lotnum_li=[]
result = ''
for _ in range(6):
    result_li=[]

    lot_nums = random.sample(range(1,46),6)
    lotnum_li.append(lot_nums)
    # 비교점..
    cnt = 0
    for n in lot_nums:
        if n in ss:
            # print(n)
            cnt += 1

        if cnt == 3:
            result = '5등임'
        elif cnt == 4:
            result = '4등임'
        elif cnt == 5:
            if 10 in lot_nums:
                result = '2등'
            result = '3등임'
        elif cnt == 6:
            result = '1등임'
        else:
                result = '꽝'
        result_li.append(result)
    
    print(result_li)