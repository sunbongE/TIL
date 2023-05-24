def dfs(n, temp):
    # print(temp, n)
    # 전체 선택됨,
    if n >= N:
        # temp에 저장된 값의 최대값이 길이과 같으면 답이다.
        max_num = max(list(map(int, temp)))
        # 사용가능한 수의 개수와 같으면으로 대체
        if max_num == sum(valid):  # len(temp) => 런타임에러
            print(*temp)
            exit()
        return

    # 1의 자리와 2의 자리 수를 조회해야한다.
    # 만약 valid에 처리가 되어있으면 2자리를 조회해야한다.
    for i in range(1, 3):
        if n + i <= N:
            num = nums[n : n + i]
            # print(num)
            if num[0] != 0:  # 왼쪽에 0이 오면 안된다.
                num = int(num)
                if num <= 50 and not valid[num]:  # 사용 가능하다면
                    valid[num] = 1
                    dfs(n + i, temp + [num])  # 더한 숫자의 개수만큼 n을 증가시킨다.
                    valid[num] = 0


nums = input()
N = len(nums)  # 입력 길이
valid = [0] * 51  # 나올 수 있는 수열 전체를 기록
dfs(0, [])
