def solution(participant, completion):
    participant.sort()  
    completion.sort()
    # print(participant,completion)
    for p,c in zip(participant,completion):
        if p != c:
            return p
        
    return participant.pop()

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])