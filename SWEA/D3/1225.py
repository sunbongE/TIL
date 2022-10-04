import sys
sys.stdin = open('1225.txt')


# 8개의 수가 주어지고 1~5까지 빼는 것을 target <= 0 이 값이 나올 때 멈춰서 출력 0은 가장 뒤로#

# 입력먼저
for _ in range(10):
    case = input()
    li = list(map(int, input().split()))
    d = 1

    while 1:
        if d >5:
            d=1

        diff = li.pop(0)-d # 앞에꺼 빼와서 1 뺌

        if diff <= 0:
            break
        li.append(diff)
        d += 1
    print(f'#{case}',end=' ')
    print(*li,0)