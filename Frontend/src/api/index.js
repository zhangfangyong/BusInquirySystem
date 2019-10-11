// import request from '@/utils/request'
import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000'

const instance = axios.create({
  baseURL: baseURL, // url = base url + request url
  timeout: 5000, // request timeout
  headers: {
    'Access-Control-Allow-Headers': 'text/html'
  }
})

export function getNews() {
  return instance.post('/Bus/news/')
}

export function getBusRoute(busid) {
  return instance.post('/Bus/busid/', JSON.stringify({ busid }))
}

export function searchRoute(startid, endid) {
  return instance.post('/Bus/searchroute/', JSON.stringify({ startid, endid }))
}

export function searchBus(stationname) {
  return instance.post('/Bus/searchbus/', JSON.stringify({ stationname }))
}
