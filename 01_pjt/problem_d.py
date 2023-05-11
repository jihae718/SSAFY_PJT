import json


def max_revenue(movies):
    id_lst=[]
    for movie in movies:
        id_lst.append(movie['id'])
        
    high = 0
    for id in id_lst:
        movie2 = open(f'data/movies/{id}.json', encoding='utf-8')
        movie3 = json.load(movie2)
        if movie3['revenue'] > high :
            high = movie3['revenue']
            title = movie3['title']
    return title
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

# 반복문을 통해 movies 폴더 내부의 파일들을 오픈
# 수익이 가장 높은 영화의 제목을 출력하는 함수 
# max_revenue를 완성합니다 : title
# 결과 => 반지의 제왕: 왕의 귀환


