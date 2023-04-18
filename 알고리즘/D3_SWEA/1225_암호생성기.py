from collections import deque

for _ in range(10):
    case = int(input())
    nums = deque(map(int, input().split()))
    temp = 0
    while nums[-1] != 0:
        for sub in range(1, 6):
            temp = nums.popleft()
            temp -= sub
            if temp <= 0:
                temp = 0
            nums.append(temp)
            if temp == 0:
                print(f"#{case}", *nums)
                break
