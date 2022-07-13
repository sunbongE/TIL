numbers = [0, 20, 100, 40]
max = numbers[0]
second = numbers[0] #음수 대비해서 변수를 0으로 저장하면 안된다.

for i in numbers:
    if i > max :
        second = max  #먼저 두번째로 큰수를 기록하고 최댓값을 넘겨야 한다.
        max = i
    elif second < i < max :
        second = i
    
print(second)

# max를 구하고 제거하고 다시 구할 생각을 했지만 아직 안 배운 명령어라서 제거나 정렬은 안했다.

# 그럼 최댓값을 구하는 과정에서 전 값이 2번째로 큰 값이다.
#   생각하고 second 변수를 만들어서 기록한 후 출력한 방법이다.