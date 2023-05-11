import json

def dec_movies(movies):
    id_lst=[]
    for movie in movies:
        id_lst.append(movie['id'])
    result = []
    for id in id_lst:
        movie2 = open(f'data/movies/{id}.json', encoding='utf-8')
        movie3 = json.load(movie2)
        if movie3['release_date'][5:7]=="12":
            result.append(movie3['title'])
    return result
            
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

# 영화 세부 정보 중 개봉일 정보(release_date) 이용
# 12월에 개봉한 영화들의 제목 리스트를 출력
# 반복문을 통해 movies 폴더 내부의 파일들을 오픈
# 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수
# original_title이 아닌 title을 사용
# ['그린 마일', '인생은 아름다워', '반지의 제왕: 왕의 귀환', '스파이더맨: 뉴 유니버스']