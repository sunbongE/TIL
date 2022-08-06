data_list = ['a','but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']

for index in range(len(data_list)) : # 리스트의 길이만큼 
    data_len = len(data_list[index]) # 길이
    data_list[index] = (data_list[index], data_len)  # 인덱스에 ('but', 3) 문자와 그 길이를 튜플로

data_list.sort(key = lambda x :(x[1], x[0])) # 오름 정렬 문자와 그 개수로  정렬기준이 문자가 첫번째 길이가 두번째인듯
print(data_list)