<template>
  <div class="mx-auto">
    <button @click="getRandomMovie" class="btn btn-success" type="button"
    style="width: 18rem;">Pick</button>
    
    <div class="card mx-auto mt-3"  v-if="selectMovie" style="width: 18rem;"
    data-bs-toggle="modal"
    :data-bs-target="`#staticBackdrop-${selectMovie?.id}`"
    >
      <img :src="'http://image.tmdb.org/t/p/w500/' + selectMovie?.poster_path" class="card-img-top justify-content-center" 
        style="width:100%; object-fit:cover;"
        alt="...">
      <div class="card-body">
        <h5 class="card-title">{{selectMovie?.title}}</h5>
      
        <p class="card-text">{{selectMovie?.overview.substr(0,100)+'...'}}
        </p>
      </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" :id="`staticBackdrop-${selectMovie?.id}`" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5 " id="staticBackdropLabel">{{selectMovie?.title}}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h5>개봉일</h5>
            {{selectMovie?.release_date}} <hr>
            <h5>줄거리</h5>
            {{selectMovie?.overview}}
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="addMovie" data-bs-dismiss="modal">찜하기</button>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>

    </div>


  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'RandomView',
  data(){
    return {
      selectMovie: null,
    }
  },
  methods:
  {
    getRandomMovie(){
      this.selectMovie = _.sample(this.$store.state.movies)
    },
    addMovie(){

      if (this.selectMovie) {
      const title = this.selectMovie.title
      const movie = {
      'watchMovie': title,
      'is_watched' : false,
      'id': this.selectMovie.id,
      }
      this.$store.dispatch('addMovie', movie)
      alert('관심목록에 추가되었습니다.')
      this.$router.push({name: 'WatchListView'})
    }

      }

  }
}
</script>

<style>

</style>