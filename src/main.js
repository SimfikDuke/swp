import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import Store from './store'

Vue.config.productionTip = false
Vue.use(Vuex)

new Vue({
  vuetify,
  router,
  data: Store,
  render: h => h(App)
}).$mount('#app')
