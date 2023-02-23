# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)
# for a in arr[::-1]:
#     if a == 0:
#         arr.remove(a)
#     else:
#         break
# # print(arr)
# cnt = 0
# for num in arr:
#     while num:
#         if num <= 1:
#             break
#         if num % 2 == 0 and 1 not in arr:
#             for i in range(len(arr)):
#                 arr[i] = arr[i] // 2
#                 num = arr[i]
#             if arr[i] <= 1:
#                 cnt += 1
#                 break
#             cnt += 1
#         elif num % 2 == 0 and 1 in arr:
#             while 1 in arr:
#                 idx = arr.index(1)
#                 arr[idx] -= 1

#         else:
#             num -= 1
#             cnt += 1
#             # print(arr)
#             # print(cnt)
#         # print(arr)
#         # print(cnt)
#         if sum(arr) == 0:
#             cnt += 1
#             break
# # print(arr)
# cnt += len(arr)
# print(cnt)


## 44ms
n = int(input())
arr = list(map(int, input().split()))

cnt = 0
while any(arr):  # arr 에 1 이상이 하나라도 있을 경우 반복
    tmp = [i for i in arr]  # 2로 나누어질 경우 저장
    print(tmp)
    print(cnt)
    for i in range(len(arr)):
        if arr[i] % 2 == 0:  # 만약 2로 나눠지면
            tmp[i] = arr[i] // 2  # tmp에 2로 나눈 결과 저장
        else:  # 나눠지지 않으면
            arr[i] -= 1  # 1을 뺌
            cnt += 1
            break
    else:  # 모두 2로 나누어지면 arr에 tmp 대입
        arr = tmp
        cnt += 1
# print(arr)
print(cnt)

# ## 40ms
# n = int(input())
# arr = list(int(x) for x in input().split())
# arr.sort()

# cnt = 0

# while sum(arr) != 0:
#     check = 0
#     for i in range(n):
#         if arr[i] % 2 != 0 or arr[i] == 0 or arr[i] == 1:
#             if arr[i] == 0:
#                 continue
#             else:
#                 arr[i] -= 1
#                 cnt += 1
#             check = 1
#     if check == 0:
#         for i in range(n):
#             arr[i] //= 2
#         cnt += 1

# print(cnt)
