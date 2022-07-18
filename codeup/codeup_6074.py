# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
c = input()
c2 = ord(c)
ord_a = ord("a")
while ord_a <= c2:
    print(chr(ord_a), end = " ")
    ord_a += 1