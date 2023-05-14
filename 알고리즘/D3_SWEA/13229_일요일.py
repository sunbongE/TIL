dogam = {"MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1, "SUN": 7}
for t in range(int(input())):
    ans = dogam[input()]
    print(f"#{t+1} {ans}")
