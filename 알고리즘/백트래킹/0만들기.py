# 0 만들기.
# 연산자 리스트를 만들어서 더하기 빼기 공백을 추가시키고
# 더하기 빼기 공백을
def dfs(n, nums):  # ['1','+','2','3']
    global ans
    if n == N:
        # print("".join(nums))
        result = eval("".join(nums).replace(" ", ""))
        if result == 0:
            ans.append("".join(nums))
        return

    nums.append(" ")
    nums.append(str(n + 1))
    dfs(n + 1, nums)
    nums.pop()
    nums.pop()

    nums.append("+")
    nums.append(str(n + 1))
    dfs(n + 1, nums)
    nums.pop()
    nums.pop()

    nums.append("-")
    nums.append(str(n + 1))
    dfs(n + 1, nums)
    nums.pop()
    nums.pop()


for _ in range(int(input())):
    ans = []
    N = int(input())
    numss = [str(i) for i in range(1, N + 1)]

    dfs(1, ["1"])
    print(*ans, sep="\n")
    print()


t = int(input())
for _ in range(t):
    n = int(input())
    op = [" ", "+", "-"]

    def cal(result):
        total = 0
        prev = (1, 1)
        for i in range(n - 1):
            if result[i] == "+":
                total += prev[0] * prev[1]
                prev = (1, i + 2)
            elif result[i] == "-":
                total += prev[0] * prev[1]
                prev = (-1, i + 2)
            else:
                x = prev[0]
                y = prev[1] * 10 + (i + 2)
                prev = (x, y)
        total += prev[0] * prev[1]
        return total

    def printcal(result):
        s = "1"
        for i in range(n - 1):
            s += result[i]
            s += str(i + 2)
        print(s)

    def backtracking(result):
        if len(result) == n - 1:
            if cal(result) == 0:
                printcal(result)
            return

        for o in op:
            result.append(o)
            backtracking(result)
            result.pop()

    backtracking([])
    print()


# -----------------
def dfs(num, result):
    global N
    if num == N:
        res = result.replace(" ", "")
        if eval(res) == 0:
            print(result)
        return

    if num < N:
        dfs(num + 1, result + " " + str(num + 1))
        dfs(num + 1, result + "+" + str(num + 1))
        dfs(num + 1, result + "-" + str(num + 1))
        # 덧셈인지 뺄셈인지 알려줘서 걔랑 값을 더해줘야됨


T = int(input())
for _ in range(T):
    N = int(input())
    dfs(1, "1")
    print()
