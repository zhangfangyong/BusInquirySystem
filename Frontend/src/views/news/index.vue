<template>
  <div>
    <div>{{ JSON.stringify(news) }}</div>
    <div>{{ JSON.stringify(busRoute) }}</div>
    <div>{{ JSON.stringify(routeInfo) }}</div>
    <div>{{ JSON.stringify(busInfo) }}</div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import store from '../../store'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters(['news', 'busRoute', 'routeInfo', 'busInfo'])
  },
  mounted() {
    store.dispatch('api/getNews')
    store.dispatch('api/getBusRoute', 'R1')
    store.dispatch('api/searchRoute', { startid: 'S1', endid: 'S5' })
    store.dispatch('api/searchBus', 'S2')
  }
}
</script>

<style scoped></style>
