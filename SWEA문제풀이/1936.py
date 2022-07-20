a,b = map(int, input().split())
가위 = 1
바위 = 2
보 = 3

if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print("A") #a가 이기는 경우
else:
    print("B")