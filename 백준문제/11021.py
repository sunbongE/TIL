case = int(input())

for test in range(1,case+1):

    a, b = map(int, input().split())
    print(f'Case #{test}: {a+b}')