# 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.
#input
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

cnt = 0

for i in students:
    if i == '이영희' :
        cnt += 1

print(cnt)
