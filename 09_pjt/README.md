# 1. 기본설정
## 주요 구조
```
my-vue-pjt
├─ src
│  ├─ App.vue
│  ├─ components
│  │  ├─ MovieCard.vue
│  │  ├─ WatchListForm.vue
│  │  └─ WatchListItem.vue
│  ├─ main.js
│  ├─ router
│  │  └─ index.js
│  ├─ store
│  │  └─ index.js
│  └─ views
│     ├─ MovieView.vue
│     ├─ RandomView.vue
│     └─ WatchListView.vue

```
## 필요한 터미널 명령어
```
$ vue create my-vue-pjt
$ vue add vuex
$ vue add router
$ npm i axios
$ npm i vuex-persistedstate
$ npm run serve
```

## public / index.html
- CSS, Javascript Bootstrap CDN 추가

## router / index.js
- 장고의 urls.py와 같은 역할을 하는 파일로, routes에 url의 path, name, component를 명시한다.
- 각 페이지로 이동시키기 위해서는 먼저 해당 파일을 컴포넌트로 임포트해와야 한다.

## store / index.js
- TMDB API 키를 여기(https://www.themoviedb.org/settings/api)에서 받아서 GET URL에 붙인다음 변수 MOVIE_URL에 저장한다
- Vuex.Store의 state에 movies, watchList 초기값을 빈 리스트로 저장하고
- dispatch명령어로 실행할 actions 메써드를 지정한다. 여기서 getMovies메써드는 MOVIE_URL에서 axios로 url을 get한다.
- 실제로 데이터(state)를 변화시키는 작업은 mutations에서 commit 명령어로 실행한다. actions함수는 camelCase로, mutations함수는 대문자로 쓴다
- actions로 안가고 바로 commit해야 할 함수는 mutations에 바로 적는다
<br><br>

# 2. views
## App
### 메뉴바
- Bootstrap 디자인을 활용하여 왼쪽에 싸피로고를 style속성으로 img 크기를 조정해서 넣고
- router에서 지정한 이름을 라우터 링크에 to 속성으로 주어서 (`router-link :to="{name:'이름'}"`) 링크로 이동가능한 Movie, Random, WatchList 메뉴를 만들었다
### `<router-view/>`
- 컴포넌트로 추가한다.
### 라이프사이클 후크
- 문서가 생성되면(created) 영화 데이터를 가져와야 한다. 상위를 가리키기 위해 this를 쓰고, store를 접근하려면 상위이므로 $를 붙여써야한다. 영화데이터를 가져오는것은 actions 메써드이므로 dispatch명령어로 가져온다.
  ```javascript
  export default({
    created(){
      this.$store.dispatch('getMovies')
    }
  })
  ```

## MovieView
- MovieCard 하나하나를 반복하며 넣어줄 구멍을 만드는 페이지다.
- 화면 크기에 따라서 한 줄에 카드가 각 1개, 2개, 3개가 보이도록 부트스트랩을 적용했다.
- `<MovieCard/>` 컴포넌트는 v-for 옵션을 줘서 movie 하나하나를 반복하는데, 이때 movie를 자식 컴포넌트인 `<MovieCard/>`에 내려주기 위해서 `:movie='movie'`와 같이 바인딩한다.
- 화면이 뜨자마자 작동하는 computed안에 movies()메쏘드를 넣어준다. `this.$store.state.movies`를 리턴한다.

## RandomView
### 무비카드
- 첫번째 div태그 안에는 Pick버튼과, Pick버튼을 누르면 나타나는 랜덤 영화 카드가 나타난다. 이 div에는 `<div class="mx-auto">`부트스트랩 옵션을 줘서 x축방향 마진을 자동으로 하면 가운데 정렬이 된다.
- Pick버튼을 만들어주는데, 여기에 `@click="메쏘드명"`으로 클릭시 발생할 이벤트를 명시한다.
- 토글시 모달 버튼이 나타나게 하려면 다음 속성을 준다
  ```html
  data-bs-toggle = "modal"
  :data-bs-target = "`#staticBackdrop-${selectMovie?.id}`"
  ```
- 무비카드에는 영화포스터 이미지, 영화 제목, 영화 줄거리 세가지 정보를 넣었다. 이미지는 `:src="'http://image.tmdb.org/t/p/w500/' + selectMovie?.poster_path"`와 같이 더하기로 가져왔고, 영화 제목과 줄거리는 있을 경우만 가져오도록 `{{selectMovie?.title}}`과 같이 `?`을 이용했다. 줄거리는 100글자 이상일 경우 100자까지만 보이고 `...`으로 마무리하도록 `{{selectMovie?.overview.substr(0,100)+'...'}}`와 같이 작성했다
- 랜덤 추출은 loadsh 라이브러리를 이용했다
  ```script
  import _ from 'lodash'
  export default {
    methods:
    {
      getRandomMovie(){
        this.selectMovie = _.sample(this.$store.state.movies)
      },
    }
  }
  ```
### 모달
- 무비카드를 선택하면 나오는 영화 상세정보를 views에 새 파일로 만들지, 모달로 구현할지 고민했다. 모달이 페이지 이동없이 더 라이트할 것 같아서 동 페이지에 부트스트랩에 있는 모달 코드르 이용해서 구현했다
- 모달과 모달이 뜨는 이벤트를 연결하려면 모달에 알아볼 수 있는 속성을 줘야 한다
  ```html
  :id="`staticBackdrop-${selectMovie?.id}`"
  ```
- 영화 상세정보에는 모달 헤더(영화 제목), 모달 바디(개봉일, 줄거리)를 넣었고, 모달 푸터에는 찜하기 버튼과 Close 버튼을 넣었다.
- 찜하기 버튼을 누르면 `addMovie` 메써드가 실행되어 watchMovie에 추가되고 `WatchListView`로 이동되도록 만들었다. 그런데 이동시켰더니 검은 그림자가 사라지지 않아서 여기에도 `data-bs-dismiss="modal"`속성을 넣었더니 해결되었다.

## WatchListView
- `<WatchListForm/>`과 `<WatchListItem/>` 자식 컴포넌트가 들어갈 구멍을 뚫어놓은 페이지다. 둘 사이에는 부트스트랩 `<ul class="list-group px-3">`을 이용하여 여백을 주었다.
- state에 있는 watchList가 변화할때마다 감시하는 computed 메써드를 만든다
  ```javascript
  export default {
    computed: {
      watchList(){
        return this.$store.state.watchList
      }
    }
  }
  ```
  <br><br>

# 3. 컴포넌트
## MovieCard
- MovieView의 자식컴포넌트로 영화 카드를 클릭하면 해당 영화의 상세페이지가 뜨는 모달이 실행된다. 
- 위의 RandomView의 카드 하나를 만든 것과 유사하다. 아까는 `selectMovie`였고 지금은 `movie`인 것만 다르다.
- 부모에게서 받는 `movie`는 props에서 `Object`로 타입을 명시해준다.
- 영화 카드 코드 아래에 모달 코드를 작성하는데, 모달에서 `찜하기`를 누르면 실행될 `addMovie` 메서드를 정의한다. 찜하면 찜이 되었다는 경고창이 뜨고 `WatchListView`로 페이지를 이동시킨다
- 카드에 마우스를 올리면 실행되는 css는 `.card:hover{}`로 지정해준다. box-shadow 속성은 다음 사이트(https://getcssscan.com/css-box-shadow-examples)에서 가져온다. cursor모양은 손바닥 모양(grab)으로 지정(`cursor:grab;`)해주었다
## WatchListForm
- 입력창에 넣는 내용을 양방향으로 적용해주려면 `v-model`을 이용한다. 이때 빈칸 입력은 거르려면 `v-model.trim="watchMovie"`와 같이 `trim`을 이용하면 된다.
- 입력창에 입력하고 엔터를 누르는 것으로도 입력이 되게 하려면 `@keyup.enter="addMovie"`와 같이 하면 된다
- data에 초기값 설정을 영화제목은 null, id는 0으로 설정했다
- 입력창에서 받은 watchMovie가 입력을 안했거나 빈칸을 제출해서 null이면 입력하라는 경고창을 띄운다. 입력값이 있으면 id를 1키워서 `this.id`로 넣고 영화 보지는 않았다는 `is_watched`값을 초기값으로 설정하고 제목은 `watchMovie`에 넣었다. 이 모든 정보는 `movie`라는 변수에 넣어서 `addMovie` actions 메써드에 dispatch할때 함께 보낸다.

## WatchListItem
- 클릭하면 완료 표시(취소선)가 되도록 이벤트 리스너를 추가한다. 영화상세정보 모달에서 받은 `watch.watchMovie`도 찜 리스트에 추가된다.
- Item 옆에 X버튼을 누르면 정말로 삭제할 것인지 확인하는 모달 창을 띄운다. '아니오' 버튼을 누르면 모달 창을 닫고, '네'버튼을 누르면 `deleteWatch(watch)`메서드를 호출하고 모달창을 닫는다. 이 함수는 store에 있는 watchList 데이터를 직접 수정하기 위해 mutations에 있는 DELETEWATCH 메서드를 실행시킨다.
  ```javascript
  deleteWatch(watch) {
    this.$store.commit('DELETEWATCH', watch)
  }
  ```
  ```javascript
  // store / index.js
  mutations: {
    DELETEWATCH(state, watch) {
    state.watchList = state.watchList.filter((watchItem)=> {
      return !(watchItem.id === watch.id)
    })
    }}
  ```
  <br><br>
# 4. 프로젝트를 마치며
뷰 공부에 어려움을 느끼고 힘들어하던 시기였는데, 페어인 동민이가 너무 상세하게 잘 알려줘서 함께 프로젝트하는 동안 재밌었고, 할 수 있겠다는 생각이 들었다. 주말동안 차근차근 복기하며 시도해봐야겠다.