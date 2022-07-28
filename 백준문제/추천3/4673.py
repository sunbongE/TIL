# # 셀프 넘버
# # 일단, 생성자가 있는 애들을 구한다.
num = set(range(1,10000))
new_num = set()

for i in num:         # '78'
    for j in str(i): 
        i += int(j) # 7 + 8
    new_num.add(i)
# print(len(new_num))
result = num - new_num
for a in sorted(result):
    print(a)
