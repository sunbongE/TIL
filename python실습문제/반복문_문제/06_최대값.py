numbers = [0, 20, 100]
max = numbers[0] #max값은 리스트 요소 중 하나로 잡는게 비교하는 대상이 더 적합하다.


for i in range(len(numbers)):
    if numbers[i] > max:

        max = numbers[i]
    
print(max)

# 최댓값을 구하려면 하나씩 비교를? 해야 하니까 아마도 for문으로 뽑아서 비교를 해야 할까?

# 인덱스 접근을 위해 range 사용해서 해봤음

# max 변수에 처음 값을 넣고 다음 수와 비교해서 큰 수를 변수에 대입 

# 처음에 number[i] > number[i+1] 시도했지만 out of range 에러로 사용이 안됨