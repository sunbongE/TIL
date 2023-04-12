dic = {
    "01": 31,
    "02": 28,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31,
}

for _ in range(int(input())):
    # 4:6
    temp = input()
    # print(temp[4:6])
    if 0 >= int(temp[4:6]) or int(temp[4:6]) > 12:
        print(f"#{_+1} -1")
    else:
        if 0 < int(temp[6:]) <= dic[temp[4:6]]:
            print(f"#{_+1} {temp[:4]}/{temp[4:6]}/{temp[6:]}")
        else:
            print(f"#{_+1} -1")
