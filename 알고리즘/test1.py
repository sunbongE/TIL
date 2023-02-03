# def multipliers():
#   return [lambda x: i * x for i in range(4)]
# print ([m(2) for m in multipliers()])


# class DefaultDict(dict):
#     def __missing__(self, key):
#         return []

# d = DefaultDict()
# d['florp'] = 127

# d = DefaultDict()
# print(f"d 1: {d}")
# print(f"d 2: {d['foo']}")

# normal = dict()
# normal['florp2'] = 127
# print(f"normal 1 : {normal}")
# print(f"normal 2 : {normal['foo']}")

# from pprint import pprint
# def solution(board, moves):
#     answer = 0
#     temp=[]

#     new_board = [[0]*len(board[0]) for _ in range(len(board))]
    
#     for i in range(len(board[0])):
#         for j in range(len(board)):
#             new_board[j][i] = board[i][j]
#     for m in moves:
#         m = m-1
#         for i in range(len(board[0])):
#             if new_board[m][i] != 0:
#                 if temp and temp[-1] != new_board[m][i]: # 마지막 값과 다르면 넣고 같으면 빼고 ans+=1
#                     temp.append(new_board[m][i])
#                 elif not temp:
#                     temp.append(new_board[m][i])
#                 elif temp and temp[-1] == new_board[m][i]:
#                     temp.pop()
#                     answer += 2

#                 new_board[m][i]=0
#                 break
#             # print(temp)
#     return answer

# def solution(board, moves):
    # cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
#     a, s = 0, [0]
#     print(cols)
#     for m in moves:
#         if len(cols[m - 1]) > 0:
#             if (d := cols[m - 1].pop(0)) == (l := s.pop()):
#                 a += 2
#             else:
#                 s.extend([l, d])

#     return a
# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

# a=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# print(*zip(*a))
