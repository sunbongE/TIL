from http.client import responses
from urllib import response
import requests
from pprint import pprint


def recommendation(title):
    # search 주소를 입력
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '5b0bce187b00bc7d98febf5046458596', # my key
        'language' : 'ko-kr', #한국어
        'query' : title # 이거 필수 사항임
    }

    res = requests.get(base_url+path, params = params).json()
    # 해당 주소에 값을 json형식으로 요청하여 받아옴
    
    # return result
    try :
        result = res.get('results')[0].get('id')
        path = f'/movie/{result}/recommendations' # 검색할 곳 주소
        res2 = requests.get(base_url+path, params = params).json()
        result2 = res2.get('results') # list안에있는 dic형태의 영화 정보들에 접근했다.
        recom_t = []
        for i in range(len(result2)):
            title = result2[i].get('title')
            recom_t.append(title)
        return recom_t
    except IndexError:
        return None

    
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
