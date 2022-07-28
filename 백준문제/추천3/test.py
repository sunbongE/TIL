#생성자 구하는 법

n = int(input())
c_num = 0
c_li = []
for x in str(n):
    print(x)
    n += int(x)
c_li.append(n)
print(c_li)