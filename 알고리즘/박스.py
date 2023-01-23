for _ in range(int(input())):
    n, m = map(int,input().split())
    box = [input().split() for _ in range(n)] # 전체 리스트 생성
    ans = 0
    for j in range(m):
        cnt = 0
        for i in range(n-1,-1,-1): # 맨 뒤 리스트부터 거꾸로 탐색
            if box[i][j] == '1':
                ans += cnt
            else:
                cnt += 1 # 인덱스 값을 찾는 대신, 0이 나올 때마다 1씩 임시 카운트 값(cnt)을 추가해주면 된다.
    print(ans)