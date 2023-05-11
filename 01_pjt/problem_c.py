import json
from pprint import pprint


def movie_info(movies, genres):
    
    big_lst = []
    
    for movie in movies:
        lst = []
        for genre in genres:
            for i in range(len(movie.get('genre_ids'))):
                if movie['genre_ids'][i] == genre['id']:
                    lst.append(genre['name'])
            
        result = {
            'genre_names' : lst,   # ['Drama', 'Crime']
            'id' : movie.get('id'),  #278 
            'overview' : movie.get('overview'),  # 촉망받는 ~
            'poster_path' : movie.get('poster_path') , #'/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg', ㅇ
            'title' : movie.get('title'), #'쇼생크탈출' 
            'vote_average' : movie.get('vote_average'), # 8.7 
        }   
            
        big_lst.append(result)
    
    return big_lst      
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
