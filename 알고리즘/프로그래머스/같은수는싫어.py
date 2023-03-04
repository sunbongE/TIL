def solution(arr):
    temp = []
    temp.append(arr[0])
    for i in range(1, len(arr)):
        if temp[-1] != arr[i]:
            temp.append(arr[i])

    return temp
