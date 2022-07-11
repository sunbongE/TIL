# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.
a, b = input().split()

b, a = a, b

print(a)
print(b)