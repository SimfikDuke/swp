import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import axios from 'axios'
export default new Vuex.Store({
  state: {
    apiUrl: 'http://localhost:5000/'
  },
  mutations: {

  },
  actions: {
    updateAuth: function () {
      if (localStorage.token) {
        axios.get(this.state.apiUrl, {
          headers: {
            Authorization: localStorage.token
          }})
            .then(response => {
              localStorage.userName = response.user.name
              localStorage.isAdmin = response.role === 777
            })
            .catch(
                response => {
                  // eslint-disable-next-line no-console
                  console.log(response)
                  localStorage.userName = null
                }
            )
      } else {
        localStorage.userName = null
      }
    }
  }
})
