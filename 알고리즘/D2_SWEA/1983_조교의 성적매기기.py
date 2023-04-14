# k 가 1부터니까 2가 나오면 인덱스 1을 찾는 문제
# 풀이 순서
# 입력
t = int(input())
st_class = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
# 모든 학생 점수를 받으면서 총점을 계산하여 총점을 담을 리스트변수에 추가시킨다.
for _ in range(t):
    n, k = map(int, input().split())
    score_li = []
    # 중간고사 * 0.35 + 기말 *0.45 + 과제 *0.2
    # 학생들 성적 입력받기
    for i in range(n):
        mid, end, ass = map(int, input().split())
        total = round(mid * 0.35 + end * 0.45 + ass * 0.2, 3)
        score_li.append(total)
    target = score_li[k - 1]
    # print("target=>", target)
    # print("score_li =>", score_li)
    score_li.sort(reverse=True)
    # print("정렬_score_li =>", score_li)
    setting = n // 10
    ans = st_class[score_li.index(target) // setting]

    print(f"#{_+1} {ans}")
