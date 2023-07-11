# # 최빈수구하기.
# for _ in range(1, 1 + int(input())):
#     case = int(input())
#     nums = list(map(int, input().split()))
#     nums.sort(reverse=True)
#     dogam = dict()
#     for num in nums:
#         dogam[num] = dogam.get(num, 0) + 1
#     target = max(dogam.values())
#     for k, v in dogam.items():
#         if v == target:
#             print(f"#{case} {k}")
#             break
