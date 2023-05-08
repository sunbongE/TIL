# 남 => 받은 수의 배수의 스위치 상태를 반대로 변경
# 여 => 받은 수의 좌우 상태가 다르면 받은 수만 변경
# 상태가 같으면 좌우 상태가 다를때까지 탐색하여 상태가 같은 것은 전부 반대 상태로
# 변경한다.
def change(num):
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1
    return


# 스위치 개수
N = int(input())
# 스위치 상태
switch = [0] + list(map(int, input().split()))
# 켜져있으면 1
# 꺼진건 0
# 학생 수
s = int(input())
# 성별, 받은 수 (남:1, 여:2)
for _ in range(s):
    sex, num = map(int, input().split())
    if sex == 1:  # 남
        for i in range(num, N + 1, num):
            change(i)
    else:  # 여
        change(num)
        # 양쪽 스위치 상태가 같으면
        for n in range(N // 2):
            if num - n < 1 or num + n > N or switch[num - n] != switch[num + n]:
                break
            if switch[num - n] == switch[num + n]:
                change(num - n)
                change(num + n)


for idx in range(1, 1 + N):
    print(switch[idx], end=" ")
    if idx % 20 == 0:
        print()


# 0 1 1 1 0 1 0 1
