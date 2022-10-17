
def func(num, cnt):
  if len(num) >= 2:
    func(str(sum(list(map(int, num)))), cnt + 1)
  else:
    if int(num) % 3 == 0:
      print(cnt)
      print("YES")
    else:
      print(cnt)
      print("NO")

x = str(input())
func(x, 0)