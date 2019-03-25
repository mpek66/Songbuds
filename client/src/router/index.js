import Vue from 'vue';
import Router from 'vue-router';
import login from '@/ui/login/login';
import home from '@/ui/home/home';
import load from '@/ui/load/load';
import create from '@/ui/create/create';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/load',
      name: 'load',
      component: load
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/create',
      name: 'create',
      component: create
    }
  ],
  mode: 'history',
});
