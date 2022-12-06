def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        s = commands[i][0] - 1 
        e = commands[i][1]
        pick = commands[i][2] - 1 
        
        status = []
        for j in range(s,e):
            status.append(array[j])
        status.sort()
        answer.append(status[pick])
    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])