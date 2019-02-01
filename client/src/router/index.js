import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Songs from '@/components/Songs';
import Login from '@/components/Login';
import Home from '@/components/Home';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Songs',
      component: Songs,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    }
  ],
  mode: 'history',
});
