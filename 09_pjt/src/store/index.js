import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const MOVIE_URL = 'https://api.themoviedb.org/3/movie/top_rated?api_key=997eb5de104f78b2d7d37a21230077bc&language=ko-KR&page=1'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    watchList: [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    ADD_MOVIE(state, movie){
      state.watchList.push(movie)
      console.log(state.watchList)
    },
    WATCHDONE(state, watch) {
      state.watchList.forEach((watchItem)=>{
        if(watchItem.id === watch.id) {
          watchItem.is_watched = !watchItem.is_watched
        }
      })
    },
    DELETEWATCH(state, watch) {
      state.watchList = state.watchList.filter((watchItem)=> {
        return !(watchItem.id === watch.id)
      })
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: MOVIE_URL,
      })
      .then((res) => {
        const movies = res.data.results
        context.commit('GET_MOVIES', movies)
      })
    },
    addMovie(context, movie){
      context.commit('ADD_MOVIE', movie)
    },
    watchDone(context, watch) {
      context.commit('WATCHDONE', watch)
    }
  },
  modules: {
  }
})
