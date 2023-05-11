import requests


def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=997eb5de104f78b2d7d37a21230077bc&language=ko-KR&page=1'   
    response = requests.get(URL).json()
    cnt = len(response['results'])
    return cnt



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
