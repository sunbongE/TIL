import calendar

x, y = map(int,input().split())
arr = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN" ]

day = calendar.weekday(2007,x,y)
print(arr[day])
