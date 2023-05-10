ㅁ  # 팰린드롬만들기.
# 홀수가 두개있으면 팰린드롬이 안된다.
# 풀이
# 사전 순으로 정렬된 도감을 순회하면서 타겟이 되는 짝수만큼만
# 결과에 추가한다.
# 다음 문자는 결과 문자의 절반에 들어간다.
# 그리고 남은 홀수 문자가 있으면 가운데에 넣어준다.
# 삽입할 때마다 도감에 기록되있는 값은 갱신해준다.

st = sorted(input())  # 정렬된 상태로
dogam = dict()
ans = ""
# 도감에 기록
for s in st:
    dogam[s] = dogam.get(s, 0) + 1

for k, v in dogam.items():
    if v > 1:
        if v % 2 == 0:  # 짝수다.
            if len(ans) == 0:  # 처음은 그냥 넣고
                ans += k * v
            else:  # 아니면 중간에 넣어야함.
                mid = len(ans) // 2
                temp = k * v
                ans = ans[:mid] + temp + ans[mid:]
            dogam[k] = 0
        elif v % 2 == 1:  # 1보다 큰데 홀수면 -1 한 값을 ans에 넣고 도감의 값은 1로 변경
            temp = k * (v - 1)
            mid = len(ans) // 2
            ans = ans[:mid] + temp + ans[mid:]
            dogam[k] = 1
check = list(dogam.values()).count(1)
if check > 1:  # 홀수가 1개 이상은 팰린드롬 못만듬
    ans = "I'm Sorry Hansoo"
else:  # 1인거를 찾아서 가운데에 넣어준다.
    for k2, v2 in dogam.items():
        if v2 == 1:
            mid = len(ans) // 2
            ans = ans[:mid] + k2 + ans[mid:]
            dogam[k2] = 0

print(ans)
# print(dogam)
