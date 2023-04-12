# 가위 1
# 바위 2
# 보   3
a, b = map(int, input().split())

if a == 3 and b == 2:
    print("A")
elif a == 2 and b == 1:
    print("A")
elif a == 1 and b == 3:
    print("A")
else:
    print("B")
