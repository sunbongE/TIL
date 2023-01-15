import heapq
import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int,input().split())) for _ in range(N)]
times.sort()

rooms = []
rooms.append(times[0][1]) # 첫번째의 끝나는 시간

for i in range(1,N):

    if times[i][0] >= rooms[0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms,times[i][1])
        
    else:
        heapq.heappush(rooms,times[i][1])
print(len(rooms))