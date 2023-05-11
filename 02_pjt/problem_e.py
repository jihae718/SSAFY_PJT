import requests
from pprint import pprint


def credits(title):
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
        URL1=f'https://api.themoviedb.org/3//movie/{movie_id}/credits'
        resp1 = requests.get(URL1, params=params1).json()
        
        # cast(출연진)
        resp1_cast = resp1['cast']
        resp1_cast_lst=[]
        for i in resp1_cast:
            if i['cast_id']<10:
                resp1_cast_lst.append(i['original_name'])

        # crew(연출진)    
        resp1_crew = resp1['crew']
        resp1_crew_lst=[]
        for i in resp1_crew:
            if i['department'] == 'Directing':
                resp1_crew_lst.append(i['original_name'])
        
        # 리턴   
        dic={}
        dic['cast'] = resp1_cast_lst
        dic['directing']= resp1_crew_lst
        return dic
    except IndexError:
        return None

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
