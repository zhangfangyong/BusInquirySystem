import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import app from './modules/app'
import settings from './modules/settings'
import api from './modules/api'
import createLogger from 'vuex/dist/logger'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    app,
    settings,
    api
  },
  getters,
  plugins: [createLogger()]
})

export default store
