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
        <v-container>
          <v-row>
            <v-col lg="9" align="left">
              <router-link to="/">Главная</router-link> |
              <router-link to="/first">Первая</router-link> |
              <router-link to="/cards">Вторая</router-link> |
              <router-link to="/tickets">Третья</router-link>
            </v-col>
            <v-col lg="3">
              <v-btn v-if="!userName" class="mButtons" @click="authDialog = !authDialog" small rounded outlined>Авторизация</v-btn>
              <v-btn v-if="!userName" class="mButtons" @click="regDialog = !regDialog" small rounded outlined>Регистрация</v-btn>
              <span v-if="userName" class="mButtons" style="font-size: 18px">Вы вошли как <b>{{ userName }}</b></span>
              <v-btn v-if="userName" class="mButtons" @click="logout" small rounded outlined>Выйти</v-btn>
            </v-col>
          </v-row>
        </v-container>
      </div>
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
    mounted () {
      this.updateAuth()
    },
    methods: {
      updateAuth: function () {
        let needReload = false
        if (localStorage.token) {
          axios
            .get(store.state.apiUrl + 'user', {
              headers: {
                Authorization: localStorage.token
              }})
            .then(response => {
              if (localStorage.userName !== response.data.user.name) {
                needReload = true
              }
              localStorage.userName = response.data.user.name
              localStorage.isAdmin = response.data.user.role == 777
              localStorage.userRole = response.data.user.role
              this.userName = response.data.user.name
            })
            .catch(
                    response => {
                      // eslint-disable-next-line no-console
                      console.log(response)
                      localStorage.userName = null
                      localStorage.isAdmin = false
                      localStorage.userRole = null
                    }
            )
                  .finally(() => {
                    this.authDialog = false
                    this.regDialog = false
                    if (needReload){
                      location.reload()
                    }
                  })
        } else {
          localStorage.userName = null
          localStorage.userRole = null
          localStorage.isAdmin = false
          this.userName = null
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
                .catch(() => this.updateAuth())
      },
      logout: function () {
        localStorage.token = null
        localStorage.userName = null
        localStorage.userRole = null
        localStorage.isAdmin = false
        this.userName = null
        this.userRole = null
        location.reload()
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
    width: 100%;
  }
  .lft {
    padding: 25px;
  }
  .mButtons {
    margin-left: 5px
  }
</style>
