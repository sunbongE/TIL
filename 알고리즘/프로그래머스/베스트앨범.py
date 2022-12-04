def solution(genres, plays):
    answer = []

    dic=dict()
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i],0)+plays[i]
        # print(plays[i])
    # print(dic)
    sorted_dict = sorted(dic.items(), key = lambda item: item[1], reverse = True) # value기분으로 내림차순 정렬
    # print(sorted_dict)
    for gen in sorted_dict: 
        test=dict()
        for j in range(len(genres)):
            if gen[0] == genres[j]:
                test[j]=test.get(-1,plays[j])
        test = sorted(test.items(), key = lambda item: item[1], reverse = True)
        # print(test)

        if len(test) > 1:
            answer.append(test[0][0])
            answer.append(test[1][0])
        else:
            answer.append(test[0][0])
    # print(answer)

            
    return answer

# solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]	)	