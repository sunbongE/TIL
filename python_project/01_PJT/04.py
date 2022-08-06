import json
from pprint import pprint


def movie_info(movie):
     f = open('data/movie.json', 'r', encoding='UTF8')
     movie1 = json.load(f)
     info = movie1


     result = {
        'id' : info.get('id'),
        'title' : info.get('title'),
        'vote_average' : info.get('vote_average'),
        'genre_ids' : info.get('genre_ids'),
        'overview' : info.get('overview')

     }
     return  result
    # 여기에 코드를 작성합니다.  
    # id, title, vote_average, overview, genre_ids  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))