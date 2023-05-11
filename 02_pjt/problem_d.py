
import requests
from pprint import pprint


def recommendation(title):
    # 제공된 영화 제목으로 TMDB 에서 영화를 검색 Search Movies 합니다
    params = {
        'api_key': '997eb5de104f78b2d7d37a21230077bc',
        'language': 'ko-KR',
        'query' : title
        }
    URL = 'https://api.themoviedb.org/3/search/movie'
    resp = requests.get(URL, params=params).json()
    # 응답받은 결과 중 첫번째 영화의 id 값을 찾아 해당 영화에 대한 추천 영화 목록 Get Recommendations 을 가져옵니다
    try:
        movie_id = resp['results'][0]['id']
        params1 = {
            'api_key': '997eb5de104f78b2d7d37a21230077bc',
            'language': 'ko-KR',
            'movie_id': movie_id,
        }
        URL1=f'https://api.themoviedb.org/3//movie/{movie_id}/recommendations'
        resp1 = requests.get(URL1, params=params1).json()
        lst=[]
        for i in resp1['results']:
            lst.append(i['title'])
        if len(lst)>0 : 
            return lst
        else:
            return []
    
    except IndexError:
        return None
        

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
