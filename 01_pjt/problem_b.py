import json
from pprint import pprint


def movie_info(movie, genres):
    lst = []
    for genre in genres:
        for i in range(len(movie.get('genre_ids'))):
            if genre['id']== movie.get('genre_ids')[i] :
                lst.append(genre['id'])

    result = {
        'genre_names' : lst,   # ['Drama', 'Crime']
        'id' : movie.get('id'),  #278 
        'overview' : movie.get('overview'),  # 촉망받는 
        'poster_path' : movie.get('poster_path') , #'/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
        'title' : movie.get('title'), #'쇼생크탈출'
        'vote_average' : movie.get('vote_average'), # 8.7
    }
    return result      

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

# print(movie.get('genre_ids')[0], type( movie.get('genre_ids')[0]))