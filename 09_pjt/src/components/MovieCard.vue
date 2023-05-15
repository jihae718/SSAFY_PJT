<template>
  <div class="col">
    <div class="card h-100"
    data-bs-toggle="modal"
    :data-bs-target="`#staticBackdrop-${movie.id}`"
    >
      <img :src="'http://image.tmdb.org/t/p/w500/' + movie.poster_path" class="card-img-top justify-content-center" 
      style="width:100%; object-fit:cover;"
      alt="Movie Poster">
      <div class="card-body">
        <h5 class="card-title">{{movie.title}}</h5>
        <p class="card-text">{{movie.overview.substr(0,100)+'...'}}</p>
      </div>
      <div class="card-footer">
        <small class="text-muted"> 평점: {{movie.vote_average}}</small>
      </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" :id="`staticBackdrop-${movie.id}`" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5 " id="staticBackdropLabel">{{movie.title}}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h5>개봉일</h5>
            {{movie.release_date}} <hr>
            <h5>줄거리</h5>
            {{movie.overview}}
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
export default {
  name: 'MovieCard',
  data() {
    return {
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    addMovie(){
      const title = this.movie.title
      const movie = {
      'watchMovie': title,
      'is_watched' : false,
      'id': this.movie.id,
      }
      this.$store.dispatch('addMovie', movie)
      alert('관심목록에 추가되었습니다.')
      this.$router.push({name: 'WatchListView'})
    }

}
}
</script>

<style>
.card:hover {
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
  cursor: grab;
}

</style>