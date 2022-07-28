#음계
#오름차순 = ascending
#내림차순 = descending
#아니면 = mixed

li = list(map(int, input().split()))
li_as = sorted(li)
li_ds = sorted(li,reverse= True)
if li == li_as:
    print('ascending')
elif li == li_ds:
    print('descending')
else:
    print('mixed')