dust = int(input())

if dust <= 30 :
    print('좋음 0')
elif dust <= 80 :
    print('보통')
elif dust <= 150:
    print('나쁨')
else:
    print('매우나쁨')