for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    avg = sum(a) // n  # 평균값
    result = 0
    for i in range(n):
        result += abs(a[i] - avg)
    # 평균 값과의 차이에 반절이 답이된다.
    print(f"#{t+1} {result//2}")
