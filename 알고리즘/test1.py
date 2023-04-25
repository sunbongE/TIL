from pprint import pprint


# 1873. 상호의 배틀필드
def find_status():  # 검증했음.
    global way
    target = ["^", "v", "<", ">"]
    for gm in game_map:
        if "^" in gm or "v" in gm or "<" in gm or ">" in gm:
            for status in gm:
                if status in target:
                    way = status
                    if now_xy == [-1, -1]:
                        find_car_xy(way)
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


def find_car_xy(way):
    global now_xy
    for x in range(H):
        for y in range(N):
            if game_map[x][y] == way:
                now_xy = [x, y]


for case in range(1, int(input()) + 1):
    way = "?"
    now_xy = [-1, -1]  # 현재 전차의 위치

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
                find_status()  # 이 함수 다녀오면 xy랑 전차가 보는 방향을 알수있음.
            find_d_idx(way)  # 이동할 방향 찾기.
            temp_xy = now_xy[:]
            while (
                0 <= temp_xy[0] + dn[d_idx][0] < H
                and 0 <= temp_xy[1] + dn[d_idx][1] < N
            ):
                # print(now_xy[0], dn[d_idx][0])
                temp_xy[0] = temp_xy[0] + dn[d_idx][0]
                temp_xy[1] = temp_xy[1] + dn[d_idx][1]
                if game_map[temp_xy[0]][temp_xy[1]] == "#":
                    break
                if game_map[temp_xy[0]][temp_xy[1]] == "*":
                    game_map[temp_xy[0]][temp_xy[1]] = "."
                    break
        elif com == "U":
            way = "^"
            game_map[now_xy[0]][now_xy[1]] = way
            find_d_idx(way)
            if 0 <= now_xy[0] + dn[d_idx][0] < H and 0 <= now_xy[1] + dn[d_idx][1] < N:
                if game_map[now_xy[0] + dn[d_idx][0]][now_xy[1] + dn[d_idx][1]] == ".":
                    # print(game_map[now_xy[0] + dn[d_idx][0]][now_xy[1] + dn[d_idx][1]])
                    game_map[now_xy[0]][now_xy[1]] = "."  # 현재 위치는 땅으로
                    now_xy[0] = now_xy[0] + dn[d_idx][0]
                    now_xy[1] = now_xy[1] + dn[d_idx][1]
                    game_map[now_xy[0]][now_xy[1]] = "^"

        elif com == "D":
            way = "v"
            game_map[now_xy[0]][now_xy[1]] = way
            find_d_idx(way)
            if 0 <= now_xy[0] + dn[d_idx][0] < H and 0 <= now_xy[1] + dn[d_idx][1] < N:
                if game_map[now_xy[0] + dn[d_idx][0]][now_xy[1] + dn[d_idx][1]] == ".":
                    game_map[now_xy[0]][now_xy[1]] = "."  # 현재 위치는 땅으로
                    now_xy[0] = now_xy[0] + dn[d_idx][0]
                    now_xy[1] = now_xy[1] + dn[d_idx][1]
                    game_map[now_xy[0]][now_xy[1]] = "v"
        elif com == "L":
            way = "<"
            game_map[now_xy[0]][now_xy[1]] = way
            find_d_idx(way)
            if 0 <= now_xy[0] + dn[d_idx][0] < H and 0 <= now_xy[1] + dn[d_idx][1] < N:
                if game_map[now_xy[0] + dn[d_idx][0]][now_xy[1] + dn[d_idx][1]] == ".":
                    game_map[now_xy[0]][now_xy[1]] = "."  # 현재 위치는 땅으로
                    now_xy[0] = now_xy[0] + dn[d_idx][0]
                    now_xy[1] = now_xy[1] + dn[d_idx][1]
                    game_map[now_xy[0]][now_xy[1]] = "<"
        elif com == "R":
            way = ">"
            game_map[now_xy[0]][now_xy[1]] = way
            find_d_idx(way)
            if 0 <= now_xy[0] + dn[d_idx][0] < H and 0 <= now_xy[1] + dn[d_idx][1] < N:
                if game_map[now_xy[0] + dn[d_idx][0]][now_xy[1] + dn[d_idx][1]] == ".":
                    game_map[now_xy[0]][now_xy[1]] = "."  # 현재 위치는 땅으로
                    now_xy[0] = now_xy[0] + dn[d_idx][0]
                    now_xy[1] = now_xy[1] + dn[d_idx][1]
                    game_map[now_xy[0]][now_xy[1]] = ">"
        # print("명령어", com, "위치", now_xy, "바라보는방향", way, "방향인덱스", d_idx)
        # pprint(game_map)
        # print("----------------------------------------------")
    print(f"#{case}", end=" ")
    for ans in game_map:
        print("".join(ans))
# 이제 그 방향으로 대포를 쏘려면 방향에 맞는 다이나믹 idx알아한다.
# 함수를 새로 만들어서 지금 방향에 맞는 인덱스를 찾고 이동하자.

# 발사한 대포가 돌로된 벽을 만나면 벽돌이 땅이되고
# 범위를 벗어나거나 철벽을 만나면 멈춤다.
