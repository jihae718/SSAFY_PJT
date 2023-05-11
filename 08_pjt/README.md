# 관통PJT08 (신동민, 김지해)

<i>AJAX 통신을 이용해서 기존 form을 대체해서 유저 팔로우, 리뷰 좋아요 기능을 구현하고, 추천 영화를 띄우는 알고리즘을 구현</i> 
<br><br>

### 1. 팔로우 / 좋아요

- JS로 처리할 것이기 때문에 form에 url이 포함될 필요가 없다
- data-userpk를 통해 속성에 사용자pk를 저장할 수 있다
- csrf 토큰은 별도로 저장해야한다

```javascript
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
```

- axios 내부에는 url, method, headers를 지정한다
  
  ```javascript
  axios({
        url: `/accounts/follow/${ userpk }/`,
        method: 'POST',
        headers: {'X-CSRFToken' : csrfToken},
      })
  ```

<br>

### 2. 영화 추천 알고리즘

- 영화평점을 정렬해서 평점 상위 10개를 출력
  
  ```python
  # movies > views.py
  @require_safe
  def recommended(request):
    popular_movie = Movie.objects.order_by('-vote_average')[:10]
    context = { 'movies': popular_movie}
    return render(request, 'movies/recommended.html', context)
  ```
  
  <br>

- 초기 구상
  
  - 영화 평점, 대중성, 영화의 장르에 가중치를 둬서 상위 10위까지 출력
    
    (영화 평점 30%, 대중성 40%, 유저의 선호 장르 10%, 현재 영화 장르 20%)
  
  - 사용자 선호 장르와 movies/detail.html에 존재하는 장르를 조합해서 총 장르 가중치 부여
  
  - movies/detail.html 밑에 추천 영화 목록 출력하고, 링크 생성
  
  - 그러나 함수에 리스트를 만들어서 저장해야 하는 등 구현 상의 문제가 발생
  
  - 해당 영화추천 알고리즘을 추후 과제로 두고, 영화 평점 정렬로 수정



### 3. 느낀점

- <strong>(동민)</strong> 영화 추천시 유의미한 필드들에 대해 가중치를 다르게 둬서 추천 알고리즘을 고도화할 수 있을 것 같은데 시간이 부족해서 하지 못한 것이 아쉽다. 최종 프로젝트에서는 추천 알고리즘을 특별하게 만들어 보고 싶다.
- <strong>(지해)</strong> 페어인 동민이가 명확하게 알고 있지 못하고 답답했던 부분들을 시원하게 알려줬다. 전체적인 흐름부터 세부적인 개념까지 친절하게 짚어준 동민이에게 너무 감사한 마음 뿐이다. 오늘 프로젝트를 처음부터 다시 만들어보고 디자인과 기능적인 부분들에 더 많은 시도들을 해보며 공부해야겠다. 