from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    # 중복 제거
    report = list(set(report))
    # user별 신고한 id저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)

    for r in report:
        # report의 첫번째 값은 신고자id 두번째는 신고당한id
        a, b = r.split()
        # 신고자가 신고한 id추가
        user[a].add(b)
        cnt[b] += 1

    for i in id_list:
        result = 0
        #     # user가 신고한 id가 k번 이상 신고당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer
    # print(user)
    # print(cnt)


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
solution(id_list, report, k)
