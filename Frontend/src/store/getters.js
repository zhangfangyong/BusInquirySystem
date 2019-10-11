const getters = {
  sidebar: state => state.app.sidebar,
  device: state => state.app.device,
  news: state => state.api.news,
  busRoute: state => state.api.busRoute,
  routeInfo: state => state.api.routeInfo,
  busInfo: state => state.api.busInfo
}
export default getters
