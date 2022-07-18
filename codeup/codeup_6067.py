
# 0이 아닌 정수 1개가 입력되었을 때,
#  음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.

a = int(input())
if a < 0 and a % 2 == 0:
    print("A")
if a < 0 and a % 2 == 1:
    print("B")
if a > 0 and a % 2 == 0:
    print("C")
if a > 0 and a % 2 == 1:
    print("D")