<template>
  <div class="app-container">
    <el-form :inline="true" class="demo-form-inline">
      <el-form-item label="查询某站点的公交车">
        <el-input v-model="station" placeholder="请输入车站名" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">查询</el-button>
      </el-form-item>
    </el-form>
    <div v-if="busInfo.length">
      <p>经过此站点的公交车有：</p>
      <el-tag v-for="item in busInfo" :key="item" type="info">{{
        item
      }}</el-tag>
    </div>
    <!-- <div>{{ JSON.stringify(busInfo) }}</div> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import store from '../../store'

export default {
  data: () => {
    return {
      station: ''
    }
  },
  computed: {
    ...mapGetters(['busInfo'])
  },
  methods: {
    onSubmit() {
      store.dispatch('api/searchBus', this.station)
    }
  }
}
</script>

<style scoped></style>
