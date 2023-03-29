N = int(input())
string = input()
ans = 0
for i in range(N):
    ans += (ord(string[i]) - 96) * 31**i
print(ans % 1234567891)
