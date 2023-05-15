<template>
  <div id="app" class="mb-5">
    <nav id="navbar-example2" class="navbar px-3 m-3">
      <a href="/movies">
        <img src="@/assets/ssafy.png" style="width:50px; object-fit:cover;" alt="">
      </a>
      <ul class="nav nav-pills">
        <li class="nav-item px-2">
          <router-link :to="{name:'MovieView'}">Movie</router-link> 
        </li>
        <li class="nav-item px-2">
          <router-link :to="{name:'RandomView'}">Random</router-link> 
        </li>
        <li class="nav-item px-2">
          <router-link :to="{name:'WatchListView'}">WatchList</router-link> 
        </li>
      </ul>
    </nav>    
    <router-view/>
  </div>
</template>

<script>
export default ({
  created() {
    this.$store.dispatch('getMovies')
  }

})
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  background: rgb(196, 222, 238);
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
