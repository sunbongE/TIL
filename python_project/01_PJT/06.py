import json
from pprint import pprint


def movie_info(movies, genres):
     m = open('data/movies.json', 'r', encoding='utf-8')
     g = open('data/genres.json', 'r', encoding='utf-8')
     g_info = json.load(g)
     ms_info = json.load(m)
     fi=[]
    # ids = ms_info['genre_ids'] # 타입이 안맞음
     for idx in range(len(ms_info)):
        ids = ms_info[idx]['genre_ids'] 
        #print(ids) #아이디들 리스트로 []
        jang = []
        

        for idd in ids:           
            # [18, 80] 하나씩    
            for dicts in g_info: #id 하나씩 dicts에 할당
                # print(dicts['id'])
                
                 if idd == dicts['id']:      # 영화 아이디에서 가져온 거랑 장르에서 가져온 번호 비교
                    jang.append(dicts['name'])  #            같으면 이름 저장 dicts['name']
        result = {
            'genre_names' : jang,
            'id' : ms_info[idx].get('id'),
            'title' : ms_info[idx].get('title'),
            'vote_average' : ms_info[idx].get('vote_average'),
            'overview' : ms_info[idx].get('overview')


        }
        fi.append(result)

     return fi
#id, title, vote_average, overview, genre_names
    # 여기에 코드를 작성합니다.  
        



        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))