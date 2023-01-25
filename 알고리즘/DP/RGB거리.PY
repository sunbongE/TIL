import sys
input = sys.stdin.readline
n = int(input())
colors = [list(map(int,input().rstrip().split())) for _ in range(n)]
for i in range(1,n):
    colors[i][0] = min(colors[i-1][1], colors[i-1][2]) + colors[i][0]
    colors[i][1] = min(colors[i-1][0], colors[i-1][2]) + colors[i][1]
    colors[i][2] = min(colors[i-1][1], colors[i-1][0]) + colors[i][2]
print(min(colors[-1]))

# 첫번째는 계산하지 않고 두번째부터 시작하여 빨간집, 초록, 파란집인 경우를
#  계산하는데 그 이전의 값들 중 같은 갯을 제외한 min을 더해주는걸 반복한다.
#  결국 빨,초,파 집을 선택한 모든 경우에 대한 최솟값만이 더해져서 나오게되며 
# 그 중에서 최솟값을 선택하면 된다.

# 3
# 26 40 83
# 49 60 57
# 13 89 99