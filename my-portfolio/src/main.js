import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import store from './store/index'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

Vue.config.productionTip = false
Vue.use(VueRouter)
new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')
