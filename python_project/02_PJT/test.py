import requests
from pprint import pprint


def credits(title):
    #주소 설정먼저~~
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '5b0bce187b00bc7d98febf5046458596',
        'query' : title,
        'language' : 'ko-kr'
    }
    # try:
    res = requests.get(base_url+path,params = params).json()
    res_id = res.get('results')[0].get('id')#첫번째 영화의 정보들에 접근하여 id 값 가져옴
    parasite_id = ''

    path2 = f'/movie/{res_id}/credits'
    res_credits = requests.get(base_url+path2, params = params).json()
    
    result = {'cast':[],'crew':[]}
    for i in range(len(res_credits.get('cast'))):
        if int(res_credits.get('cast')[i].get('cast_id')) < 10:
            result.get('cast').append(res_credits.get('cast')[i].get('name'))
        
        if res_credits.get('crew')[i].get('department') == "Directing":
            result.get('crew').append(res_credits.get('crew')[i].get('name'))

    return len(res_credits.get('crew'))
     
    # except IndexError:
    #     return None

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
