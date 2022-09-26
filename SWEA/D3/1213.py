# Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.
import sys
sys.stdin = open("1213.txt","r",encoding="utf-8")

for _ in range(10):
    case = input()
    search_ = input()
    st = input()

    state = True
    cnt = 0 
    while state:
        if search_ in st:
            cnt += 1
            new_ = st.replace(search_,'',1)
            st = new_
        else: state = False
    print(f'#{case} {cnt}')

