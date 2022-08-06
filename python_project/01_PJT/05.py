import json
from pprint import pprint
# - 영화 데이터 `movie.json` 와 `genres.json` 을  활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
#     - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
#     - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# - `id`, `title,` `vote_average`, `overview`, `genre_names`로 결과를 만듭니다. **(결과 예시 참고)**
#     - genre_names는 각 장르 정보를 값으로 가집니다.
#     - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

def movie_info(movie, genres):
    m = open('data/movie.json', 'r', encoding='utf-8')
    g = open('data/genres.json', 'r', encoding='utf-8')
    g_info = json.load(g)
    m_info = json.load(m)
    
    ids = m_info['genre_ids']
    jang = []

    for id in ids:
        # 18, 80
    
        for dicts in g_info:
           # print(dicts['id'])
            if id == dicts.get('id'): #같으면 이름 저장 dicts['name']
                jang.append(dicts['name'])
    
    
    jang_result = jang
    
    result = {
        'genre_names' : jang_result,
        'id' : m_info.get('id'),
        'title' : m_info.get('title'),
        'vote_average' : m_info.get('vote_average'),
        
        'overview' : m_info.get('overview')

     }
    
    return result

            # for j in dicts:
            #     print(dicts[j]) #아이디추출
        


    
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))