// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import app from './app';
import router from './router';
import BootstrapVue from 'bootstrap-vue';
import VueSession from 'vue-session';

import { library } from '@fortawesome/fontawesome-svg-core';
import { faCoffee, faTimes, faPlus } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
library.add(faCoffee);
library.add(faTimes);
library.add(faPlus);

Vue.use(VueSession)
Vue.use(BootstrapVue);
Vue.component('fa', FontAwesomeIcon);

Vue.config.productionTip = false;

Vue.prototype.$eventHub = new Vue(); // Global event bus

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { app },
  template: '<app/>',
});
