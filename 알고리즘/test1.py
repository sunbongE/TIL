def find_status():  # 검증했음.
    global way
    target = ["^", "v", "<", ">"]
    for gm in game_map:
        if "^" in gm or "v" in gm or "<" in gm or ">" in gm:
            for status in gm:
                if status in target:
                    way = status
                    return


def find_d_idx(now_way):
    global d_idx
    if now_way == "^":  # 위
        d_idx = 0
    elif now_way == "v":  # 아래
        d_idx = 1
    elif now_way == "<":  # 왼
        d_idx = 2
    elif now_way == ">":  # 오른
        d_idx = 3


for case in range(1, int(input()) + 1):
    way = "?"
    H, N = map(int, input().split())
    # [상, 하, 좌, 우] 방향을 바꿀 다이나믹 인덱스
    dn = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    d_idx = 0
    # 위: 0 , 아래:1, 왼:2, 오른:3
    # 맵
    game_map = [list(map(str, input())) for _ in range(H)]

    L = int(input())
    command = input()
    for com in command:
        # s면 현재 방향에서 대포를 발사한다.
        if com == "S":
            # 만약 현재 방향을 모르면 찾아야한다.
            if way == "?":
                find_status()
            # 이제 그 방향으로 대포를 쏘려면 방향에 맞는 다이나믹 idx알아한다.
            # 함수를 새로 만들어서 지금 방향에 맞는 인덱스를 찾고 이동하자.
            find_d_idx(way)

        # 발사한 대포가 돌로된 벽을 만나면 벽돌이 땅이되고
        # 범위를 벗어나거나 철벽을 만나면 멈춤다.
