<template>
  <div class="app-container">
    <el-form :inline="true" class="demo-form-inline">
      <el-form-item label="查询公交线路">
        <el-input v-model="input" placeholder="请输入公交车ID" />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">查询</el-button>
      </el-form-item>
    </el-form>
    <div v-if="busRoute.length">
      <p>此公交车站点情况如下：</p>
      <el-steps :space="200" :active="active" finish-status="success">
        <el-step v-for="station in busRoute" :key="station" :title="station" />
      </el-steps>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import store from '../../store'

export default {
  data: function() {
    return {
      input: ''
    }
  },
  computed: {
    ...mapGetters(['busRoute'])
  },
  methods: {
    onSubmit() {
      store.dispatch('api/getBusRoute', this.input)
    }
  }
}
</script>

<style scoped></style>
