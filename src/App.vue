<template>
  <div id="app">
    <v-dialog
            v-model="authDialog"
            width="300"
    >
      <v-card class="lft">
        <v-text-field v-model="logLogin" label="Логин"></v-text-field>
        <v-text-field v-model="logPassword" label="Пароль"></v-text-field>
        <v-btn @click="login" rounded width="100%">Войти</v-btn>
      </v-card>
    </v-dialog>
    <v-dialog
            v-model="regDialog"
            width="300"
    >
      <v-card class="lft">
        <v-text-field v-model="regName" label="Ваше имя"></v-text-field>
        <v-text-field v-model="regLogin" label="Логин"></v-text-field>
        <v-text-field v-model="regPassword" label="Пароль"></v-text-field>
        <v-btn rounded width="100%" @click="register">Зарегистрироваться</v-btn>
      </v-card>
    </v-dialog>
    <v-app-bar app>
      <div id="nav">
        <div>
        <router-link to="/">Главная</router-link> |
        <router-link to="/first">Первая</router-link> |
        <router-link to="/cards">Вторая</router-link> |
        <router-link to="/tickets">Третья</router-link>
        <v-btn style="margin-left: 30px" @click="authDialog = !authDialog" small rounded outlined>Авторизация</v-btn>
        <v-btn style="margin-left: 30px" @click="regDialog = !regDialog" small rounded outlined>Регистрация</v-btn>
        <span v-if="userName" style="margin-left: 30px">Добро пожаловать, {{ userName }}</span>
      </div></div>
    </v-app-bar>
    <v-content>
      <router-view/>
    </v-content>
  </div>
</template>
<script>
import axios from 'axios'
import store from '../src/store'
  export default {
    name: "App",
    data () {
      return {
        userName: null,
        authDialog: false,
        regDialog: false,
        logLogin: '',
        logPassword: '',
        regName: '',
        regLogin: '',
        regPassword: ''
      }
    },
    methods: {
      updateAuth: function () {
        if (localStorage.token) {
          axios.get(store.state.apiUrl + 'user', {
            headers: {
              Authorization: localStorage.token
            }})
                  .then(response => {
                    localStorage.userName = response.user.name
                    localStorage.isAdmin = response.role === 777
                    this.userName = response.user.name
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
      },
      login: function () {
        axios
                .post(store.state.apiUrl + 'login', {
                  login: this.logLogin,
                  password: this.logLogin,
                })
                .then(response => {
                  localStorage.token = response.data.token
                  this.updateAuth()
                })
      },
      register: function () {
        axios
                .post(store.state.apiUrl + 'register', {
                  login: this.regLogin,
                  name: this.regName,
                  password: this.regPassword,
                })
                .then(response => {
                  localStorage.token = response.data.token
                  this.updateAuth()
                })
      }
    }
  }
</script>
<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  #nav {
    padding: 30px;
  }
  .lft {
    padding: 25px;
  }
</style>
