from django.shortcuts import render
import random
# Create your views here.
def lot(request):
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


    context = {
        'lotnum_1': lotnum_li[0], 
        'lotnum_2': lotnum_li[1], 
        'lotnum_3': lotnum_li[2], 
        'lotnum_4': lotnum_li[3], 
        'lotnum_5': lotnum_li[4], 
        'lotnum_6': lotnum_li[5], 
        'result1': result_li[0],
        'result2': result_li[1],
        'result3': result_li[2],
        'result4': result_li[3],
        'result5': result_li[4],
        'result6': result_li[5],
    }
    return render(request, 'index.html', context)