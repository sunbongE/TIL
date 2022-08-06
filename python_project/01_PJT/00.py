with open ('test.txt', 'w', encoding= 'utf-8') as f:

    f.write('2회차 박태호\nHello, Python!\n')
    for i in range(1,6):
        f.write(f'{i}일차 파이썬 공부 중\n')




