import requests
from pprint import pprint


def vote_average_movies():
    BASE_URL = 'https://api.themoviedb.org/3'

    path = '/movie/popular'
    params = {
        'api_key': '5b0bce187b00bc7d98febf5046458596',
           }

    response = requests.get(BASE_URL+path,params = params).json()   #요청한 것을 get(주소, 키)으로 받을건데 이것을 json형식으로 가져옴  
    result_list = []
    for i in range(len(response.get('results'))):   # 전체 리스트 타입이며 그 안에 있는 딕셔너리를 순회할 예정 
      result = response.get('results')[i].get('vote_average') # 딕셔너리에서 평점(키) 자료의 값을 result변수에 할당
      if int(result) >= 8:                                    # 평점이 8이상이면 참
        result_list.append(response.get('results')[i])       # 평점 8점 이상은 리스트에 딕셔너리 저장 저장   


    return result_list
   

    
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """
