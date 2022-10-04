import sys
sys.stdin = open('1225.txt')


T = 10
for t in range(1, T+1):
    tc = int(input())
    queue = list(map(int, input().split()))
    print(queue)
    i = 1
    while True:
        if i > 5:
            i = 1
        t = queue.pop(0) - i
        
        # print(t)
        if t <= 0:
            queue.append(0)
            break
        queue.append(t)
        # print(t)

        i += 1
    print(queue)
