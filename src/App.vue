<template>
  <div id="app">
    <v-dialog
            v-model="authDialog"
            width="300"
    >
      <v-card class="lft">
        <v-text-field label="Логин"></v-text-field>
        <v-text-field label="Пароль"></v-text-field>
        <v-btn rounded width="100%">Войти</v-btn>
        <v-btn rounded width="100%">Зарегистрироваться</v-btn>
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
      </div></div>
    </v-app-bar>
    <v-content>
      <router-view/>
    </v-content>
  </div>
</template>
<script>
  export default {
    name: "App",
    data () {
      return {
        userName: null,
        authDialog: false
      }
    },
    methods: {

      updateAuth: function () {
        if (localStorage.token) {
          this.userName = localStorage.userName
        } else {
          this.userName = null
        }
      },
      login: function () {

      },
      register: function () {

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
