from datetime import datetime

# print(datetime.now())
# Now = datetime.now()
# print(Now.minute == 7)
# go=0
# if Now.weekday() == 2 and Now.hour==23 and Now.minute == 55:
#     go=1
# else:go=0


# @tasks.loop(hours=1)
# async def send_sunday_notification():
#     # 현재 시간과 요일 확인
#     Now = datetime.now()
#     # weekday = Now.weekday()
#     # hour = Now.hour
#     if Now.weekday() == 3 and Now.minute == 7:
#         print(11)
Now = datetime.now()
sunday = Now.weekday()
print(Now.hour == 0, sunday == 3)

# @tasks.loop(minute=1)
#   async def printer(self):
#     Now = datetime.now()
#     sunday = Now.weekday()
#     T = Now.hour
#     if sunday == 10 and T ==0:
#       channel = client.get_channel(1091978809110171682)
#       await channel.send("일요일 오후 4시입니다! 이번 주 일정을 확인하세요.")
