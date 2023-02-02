
# def to_days(date):
#     year, month, day = map(int, date.split("."))
#     return year * 28 * 12 + month * 28 + day

# def solution(today, terms, privacies):
#     months = {v[0]: int(v[2:]) * 28 for v in terms}
#     today = to_days(today)
#     expire = [
#         i + 1 for i, privacy in enumerate(privacies)
#         if to_days(privacy[:-2]) + months[privacy[-1]] <= today
#     ]
#     return expire

# 내풀이..
def solution(today, terms, privacies):
    answer = []
    dic_terms = dict()
    today = (int(today[:4])*336) + (int(today[5:7])*28)+int(today[8:10])
    
    for i in range(len(terms)):
        k,v = terms[i].split()
        dic_terms[k] = int(v)
        
    for i in range(len(privacies)):
        temp = (336 * int(privacies[i][:4])) + (28*int(privacies[i][5:7])) + int(privacies[i][8:10]) + (dic_terms[privacies[i][-1]]*28)
        if temp-1 < today:
            
            answer.append(i+1)
            
    return answer
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
)
