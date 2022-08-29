import random
from secrets import choice

menu = ['라면', '다이어트도시락','갈비탕','돈까스','치킨','김밥']
외식 = ['치킨','족발','파스타','곱창','양꼬치&꿔바로우','떡볶이']
# print(choice(menu))
for _ in range(7):
    print(choice(외식))
