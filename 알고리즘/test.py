n, k = map(int, input().split())
result = []
nums = [a for a in range(1, n + 1)]
c = 0
idx = 0
while len(nums) > 0:
    idx = (idx + k - 1) % len(nums)
    result.append(str(nums.pop(idx)))

print("<", end="")
print(", ".join(result), end="")
print(">")
