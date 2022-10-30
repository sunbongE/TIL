# from itertools import permutations

# N, M = map(int, input().split())
# numlist = list(map(int, input().split()))
# case = sorted(set(permutations(numlist, M)))

# for i in case:
#     for j in i:
#         print(j, end=" ")
#     print()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()