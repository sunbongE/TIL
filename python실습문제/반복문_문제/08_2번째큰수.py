numbers = [0, 20, 100]
max = 0
second = 0

for i in numbers:
    if i > max :
        second = max
        max = i
    
print(second)

# max를 구하고 제거하고 다시 구할 생각을 했지만 아직 안 배운 명령어라서 제거나 정렬은 안했다.

# 그럼 최댓값을 구하는 과정에서 전 값이 2번째로 큰 값이다.
#   생각하고 second 변수를 만들어서 기록한 후 출력한 방법이다.