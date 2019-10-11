import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Layout from '@/layout'

export const constantRoutes = [
  {
    path: '/',
    component: Layout,
    redirect: '/news',
    children: [
      {
        path: 'news',
        name: 'news',
        component: () => import('@/views/news/index'),
        meta: { title: '新闻', icon: 'message' }
      }
    ]
  },
  {
    path: '/bus',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'bus',
        component: () => import('@/views/bus/index'),
        meta: { title: '公交线路查询', icon: 'dashboard' }
      }
    ]
  },
  {
    path: '/route',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'route',
        component: () => import('@/views/route/index'),
        meta: { title: '乘车线路查询', icon: 'drag' }
      }
    ]
  },
  {
    path: '/station',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'station',
        component: () => import('@/views/station/index'),
        meta: { title: '公交站点查询', icon: 'list' }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true },
  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  }
]

const createRouter = () =>
  new Router({
    // mode: 'history', // require service support
    scrollBehavior: () => ({ y: 0 }),
    routes: constantRoutes
  })

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
