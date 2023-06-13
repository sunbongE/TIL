n = int(input())
U = []
# 교집합 입력
for _ in range(n):
    U.append(int(input()))
U.sort()
# 투 포인터
while True:
    target = U.pop()

    for i in range(len(U)):
        left = i
        right = len(U) - 1

        while left <= right:
            temp = U[i] + U[left] + U[right]

            if temp < target:
                left += 1
            elif temp > target:
                right -= 1
            else:
                print(temp)
                exit()
