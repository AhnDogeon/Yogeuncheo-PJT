import Vue from 'vue'
import VueRouter from 'vue-router'
import YoGeunCheoPage from '../components/pages/YoGeunCheoPage'
import MapPage from '../components/pages/MapPage'

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: YoGeunCheoPage, name: 'home' },
    { path: '/maps', component: MapPage, name: 'map' },
  ],
});

export default router