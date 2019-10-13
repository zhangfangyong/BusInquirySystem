<template>
  <div class="app-container">
    <el-carousel height="150px">
      <el-carousel-item v-for="item in news" :key="item">
        <div class="notify">
          <div>公交新闻</div>
          <br>
          <div>标题： {{ item.title }}</div>
          <div>内容： {{ item.content }}</div>
          <div>时间： {{ item.time }}</div>
        </div>
      </el-carousel-item>
    </el-carousel>
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
  }
}
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.notify {
  /* margin-left: 20%;
  padding-top: 50px */
  margin-top: 25px;
  text-align: center;
  /* font-size: 20px; */
}
</style>
