<template>
  <div class="app-container">
    <el-form :inline="true" class="demo-form-inline">
      <el-form-item label="请输入起点">
        <el-input v-model="startid" placeholder="起点站台" />
      </el-form-item>
      <el-form-item label="请输入终点">
        <el-input v-model="endid" placeholder="终点站台" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">查询</el-button>
      </el-form-item>
    </el-form>
    <div
      v-if="
        typeof routeInfo === 'object' && routeInfo.transferTimes !== undefined
      "
    >
      <p>换乘次数为 {{ routeInfo.transferTimes }}</p>
      <p>路线站点与线路情况如下：</p>
      <el-steps
        :space="100"
        direction="vertical"
        :active="active"
        finish-status="success"
      >
        <el-step
          v-for="route in routesKeys"
          :key="route"
          :title="route"
          :description="routeInfo[route].join('->')"
        />
      </el-steps>
    </div>
    <!-- <div>{{ JSON.stringify(routeInfo) }}</div> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import store from '../../store'

export default {
  data: () => {
    return {
      startid: '',
      endid: ''
    }
  },
  computed: {
    ...mapGetters(['routeInfo']),
    routesKeys() {
      if (this.routeInfo && this.routeInfo.transferTimes !== undefined) {
        const routesMap = Object.assign(this.routeInfo)
        delete routesMap.transferTimes
        return Object.keys(routesMap)
      } else return []
    }
  },
  methods: {
    onSubmit() {
      store.dispatch('api/searchRoute', {
        startid: this.startid,
        endid: this.endid
      })
    }
  }
}
</script>

<style scoped></style>
