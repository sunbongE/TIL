# 1~5 까지 빙고판
# 빙고 3개 이상이면 빙고를 외침.
dogam = dict()  # 기록할 사전.
cnt = 0
# 1~5를 입력받을 때 i,j를 같이 기록받는다. 2중반복
for i in range(5):
    inp = input().split()
    for j in range(5):
        dogam[inp[j]] = str((i, j))

# 입력은 미리 받은 다음
command = [list(map(int, input().split())) for _ in range(5)]

# 2중 반복으로 하나씩 뽑고 뽑은 값은 key가 되어 수의 위치를 반환한다. 두번째 반복문안에 cnt+=1 이게 답이 될 것
for ii in range(5):
    for jj in range(5):
        cnt += 1
        key = str(command[ii][jj])
        vals = dogam[key]
        ti = vals[1]
        tj = vals[4]
        if ti == tj:  # 대각선
            dogam["diag"] = dogam.get("diag", 0) + 1
        if int(ti) + int(tj) == 4:
            dogam["diag2"] = dogam.get("diag2", 0) + 1

        dogam[str((ti, "_"))] = dogam.get(str((ti, "_")), 0) + 1
        dogam[str(("_", tj))] = dogam.get(str(("_", tj)), 0) + 1

        if list(dogam.values()).count(5) >= 3:
            print(cnt)
            exit()


# 수의 위치를 받으면 i,j 값에 맞는 위치에 넣어야하는데
# (i,_) (j,_)형태로 사전에 get 0 + 1해준다.
# 이렇게 사전이 들어오면 values 중에 5가 3개있으면 빙고를 외치게한다.
