// eslint-disable-next-line
import { getNews, getBusRoute, searchRoute, searchBus } from '@/api/index'

const state = {
  news: [],
  busRoute: [],
  routeInfo: {},
  busInfo: {}
}

const mutations = {
  SET_NEWS: (state, news) => {
    state.news = news
  },
  SET_BUS_ROUTE: (state, busRoute) => {
    state.busRoute = busRoute
  },
  SET_ROUTE_INFO: (state, routeInfo) => {
    state.routeInfo = routeInfo
  },
  SET_BUS_INFO: (state, busInfo) => {
    state.busInfo = busInfo
  }
}

const actions = {
  getNews({ commit }) {
    return new Promise((resolve, reject) => {
      getNews()
        .then(response => {
          const { data } = response
          commit('SET_NEWS', data)
          resolve(data)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  getBusRoute({ commit }, busid) {
    return new Promise((resolve, reject) => {
      getBusRoute(busid)
        .then(response => {
          const { data } = response
          commit('SET_BUS_ROUTE', data && data[busid])
          resolve(data && data[busid])
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  searchRoute({ commit }, routeQuery) {
    return new Promise((resolve, reject) => {
      searchRoute(routeQuery.startid, routeQuery.endid)
        .then(response => {
          const { data } = response
          commit('SET_ROUTE_INFO', data)
          resolve(data)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  searchBus({ commit }, station) {
    return new Promise((resolve, reject) => {
      searchBus(station)
        .then(response => {
          const { data } = response
          commit('SET_BUS_INFO', data && data.passid)
          resolve(data && data.passid)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
