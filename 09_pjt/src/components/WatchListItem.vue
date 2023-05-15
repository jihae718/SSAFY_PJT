<template>
    <li @click="watchDone(watch)" :class="{'done': watch.is_watched}"
    class="list-group-item hov"
    >{{watch.watchMovie}}
    <button type="button" class="d-inline btn btn-sm btn-dark" data-bs-toggle="modal" :data-bs-target="`#deleteModal-${watch.id}`">x</button>

    <!-- 모달 -->
    <div class="modal fade" :id="`deleteModal-${watch?.id}`" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="deleteModalLabel">알림</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            정말로 삭제하시겠습니까?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">아니오</button>
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="deleteWatch(watch)">네</button>
          </div>
        </div>
      </div>
    </div>


    </li>
</template>

<script>

export default {
  name: 'WatchListItem',
  props: {
    watch: Object,
  },
  methods: {
    watchDone(watch) {
      this.$store.dispatch('watchDone', watch)
    },

    deleteWatch(watch) {
      this.$store.commit('DELETEWATCH', watch)
    }
  }
}
</script>

<style>
.hov:hover {
  color: gray;
}

.done {
  text-decoration: line-through;
  background-color: rgba(184, 207, 181, 0.644);
  color: aliceblue;
}

</style>