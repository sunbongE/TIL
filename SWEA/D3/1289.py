T = int(input())                        # 테스트케이스 입력받음
for tc in range(1, T+1):                # 반복
    init = list(input())                # 원래 값을 입력받음
    n = ['0']*len(init)                 # 원래값의 길이 만큼 0을 생성
    cnt = 0 
    for i in range(len(n)):             #
        if n[i] != init[i]:             # 자리수가 다르면
            n[i:] = init[i]*len(n[i:])  # 원래 값의 자리수에 있는 수를 초기값 슬라이싱 한 수만큼 생성하여 할당
            cnt += 1                    # if문 수행 횟수는 값을 바꾼 횟수
    print('#{} {}'.format(tc, cnt))