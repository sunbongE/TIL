from django.shortcuts import render
import random
# Create your views here.

def oddeven(request, number):
    
    if number != 0 and number % 2 == 0:
        result = '짝수'
    elif number % 2 == 1:
        result = '홀수'
    elif number == 0:
        result = '0'
    
    context = {
        'result':result,
        'number':number,
    }

    return render(request,'is-odd-even.html', context)

def req_oper(request):


    return render(request,'req-oper.html')

def oper(request,num1,num2):
    plus = num1+num2
    minus = num1 - num2
    product = num1 * num2
    division = num1 // num2

    context = {
        'plus':plus,
        'minus':minus,
        'product':product,
        'division':division,

        'num1':num1,
        'num2':num2,

    }
    return render(request,'oper.html', context)

def urname(request):
    return render(request,'urname.html')

def result(request):

    items = ['개','소','돼지','말','청설모','다람이','고양이','이번생이 처음']

    name = request.GET.get('name')

    ran = random.choice(items)

    context = {
        'name':name,
        'ran':ran,
    }

    return render(request, 'result.html',context)


def lorem_input(request):

    return render(request,'lorem_input.html')

def lorem(request):

    st = ['강아지','고양이','소','말','망아지','돼지','표범']

        

    cnt = request.GET.get('q1')
    leng = request.GET.get('q2')
    print(cnt)
    print(leng)

    result = []

    for _ in range(int(cnt)):
        word=''
        for _ in range(int(leng)):
            r = random.choice(st)
        # print(r)
            word += r+' '
        result.append(word)



    context = {
        'result':result
    }

    return render(request,'lorem.html',context)