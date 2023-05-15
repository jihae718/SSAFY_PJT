<template>
  <div>
    <WatchListForm/>
    <ul class="list-group px-3">
    <WatchListItem
      v-for="(watch,idx) in watchList" :key="idx"
      :watch='watch'
    />
    </ul>

  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'

export default {
  name: 'WatchListView',
  components: {
    WatchListForm,
    WatchListItem,
  },
  computed: {
    watchList(){
      return this.$store.state.watchList
    }
  }

}
</script>

<style>

</style>