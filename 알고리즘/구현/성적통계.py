for n in range(int(input())):
    li=list(map(int,input().split()))
    point = sorted(li[1:])
    # print(point)
    # print(li)
    max_p = point[-1]
    min_p = point[0]
    gap=0
    for i in range(1,li[0]):
        if point[i] - point[i-1] > gap:
            gap =  point[i] - point[i-1] 

    print(f"Class {n+1}")
    print(f"Max {max_p}, Min {min_p}, Largest gap {gap}")