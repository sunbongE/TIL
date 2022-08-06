
delta_x = [1, -1, 0, 0]
delta_y = [0, 0, 1, -1]

x, y = 1, 1

for d in range(4):
    탐색_y = y + delta_y[d]
    탐색_x = x + delta_x[d]
    # print(탐색_x,탐색_y)

a = ['.','*']
print(*a,sep='')