<template>
  <div style="margin-bottom: 10px">
    <h2>보고싶은 영화</h2>
    <input type="text" v-model.trim="watchMovie" 
    @keyup.enter="addMovie" class="m-1">
    <button @click="addMovie" >Add</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data(){
    return {
      watchMovie: null,
      id: 0,
    }
  },
  methods: {
    addMovie(){
      const watchMovie = this.watchMovie

      if (watchMovie) {
        this.id++
        const movie = {
        'watchMovie': watchMovie,
        'is_watched' : false,
        'id': this.id,
        }
        this.$store.dispatch('addMovie', movie)
        this.watchMovie = null
      } else {
        alert('영화 입력 안 해?')
      }
    }
  },
}
</script>

<style>

</style>