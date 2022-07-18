# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는
# 코드의 일부분 입니다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#오류코드
# ```python
# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)
# ```




from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if  not fruit in fruit_count:
        fruit_count[fruit] = fruit_count.get(fruit, 1)  #fruit_count 에 계속 대입만 되고 있어서 원하는 결과가 안나옴 즉, 추가를 해야함
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)