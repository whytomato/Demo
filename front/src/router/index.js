import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
  },
  {
    path: '/register',
    name: 'register',
    component: function () {
      return import('../views/RegisterView.vue')
    }
  },
  {
    path: '/test',
    name: 'test',
    component: function () {
      return import('../views/test.vue')
    }
  },
  {
    path: '/button',
    name: 'button',
    component: function () {
      return import('../views/Button.vue')
    }
  },
  {
    path: '/login',
    name: 'login',
    component: function () {
      return import('../views/Login.vue')
    }
  },
  {
    path: '/test1',
    name: 'test1',
    component: function () {
      return import('../views/testregister.vue')
    }
  },
  {
    path: '/test9',
    name: 'test9',
    component: function () {
      return import('../views/Test/test9.vue')
    }
  },
  {
    path: '/test10',
    name: 'test10',
    component: function () {
      return import('../views/Test/test10.vue')
    }
  },
  {
    path: '/sidebar',
    name: 'sidebar',
    component: function () {
      return import('../views/Test/sidebar.vue')
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
