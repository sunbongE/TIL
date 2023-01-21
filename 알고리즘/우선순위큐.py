import heapq    
def heapsort(iterable):
    h = []
    result = []
    # 모든 원고흫 차례대로 힙에 삽입
    for val in iterable:
        heapq.heappush(h,val)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
res = heapsort(arr)

print(res)