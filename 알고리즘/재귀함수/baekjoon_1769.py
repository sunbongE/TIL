
def replay(ns,cnt): # 6000ms
    if int(ns) < 10:
        if int(ns) % 3 == 0:
            print(cnt,'YES',sep='\n')
        else:
            print(cnt,'NO',sep='\n')
        return
    new=0
    for n in str(ns):
        new += int(n)
    ns = new
    cnt+=1
    replay(ns,cnt)        
replay(input(),0)

# str함수는 시간 복잡도가 O(log n) 이고
# len은 상수 복잡도를 가진다. O(1)
# 형 변환하고 for문을 돌렸으니 위보다는 당연히 줄어든다.
# 위 if 문에서 int -> len으로만 바꿔도 차이가 클것이다.
#  #

def func(num, cnt): # 188ms
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