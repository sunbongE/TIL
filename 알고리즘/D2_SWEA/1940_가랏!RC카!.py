# 시간은 1초부터 시작이고
# 가속을 이후 속도를 이동거리에 +=
# 감속도 마찬가지다.
# 유지라면 현재속도를 이동거리에 더한다.


for _ in range(int(input())):
    n = int(input())
    # 변수: 현재 속도, 이동거리, 시간
    sec = 1  # 시간
    speed = 0  # 속도
    dis = 0  # 거리

    for __ in range(n):
        info = list(map(int, input().split()))
        # 유지가 아닐때
        if len(info) > 1:
            com, sp = info
            if com == 1:  # 가속
                speed += sp

            else:
                speed -= sp
                if speed < 1:
                    speed = 0
        dis += speed
    print(f"#{_+1} {dis}")
