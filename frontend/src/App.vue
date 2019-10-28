<template>
  <v-app id="app">
    <v-container class="container-box">
      <v-layout justify-end class="login-btn">
        <v-dialog v-model="$store.state.authDialog">
          <template v-slot:activator="{ on }">
            <v-btn text v-on="on">
              로그인
            </v-btn>
          </template>
          <UserAuth style="width: 60%; margin: auto; height: 500px;"/>
        </v-dialog>
      </v-layout>
      <router-link :to="{name: 'home'}" style="text-decoration: none; color: black;">
        <v-layout class="layout-box mt-10" justify-center>
          <p style="margin-left: 7vw;">
            요 근 처
          </p>
          <img src="./assets/yo1.png" alt="yo1" class="yo-img1">
          <img src="./assets/yo2.png" alt="yo2" class="yo-img2">
        </v-layout>
      </router-link>
      <router-view/>
    </v-container>

    <!-- each pages will be placed here -->

  </v-app>
</template>

<script>
  import UserAuth from "./components/pages/UserAuth";
  import router from './router';

  export default {
        components: {
            UserAuth
        },
        data: () => ({
            drawer: null,
            choices: [
                {
                    icon: "mdi-account-circle",
                    text: "유저 정보",
                    path: "user-search"
                },
            ],
        }),
        computed: {
          userInfo() {
              return this.$store.state.data.userInfo
          }
        },
        mounted() {
            const userInfo = localStorage.getItem('userInfo');
            this.$store.commit('data/getUserInfo', JSON.parse(userInfo));
        },
        methods: {
            goTo: function (path) {
                if (path === 'user-detail')
                    router.push({name: path ,params: {"user_id": this.userInfo.id}});
                else
                    router.push({name: path});
            },
            logout() {
                this.$store.commit('data/logout');
            },
        }
    };
</script>

<style>
    #app {
    background-color: #F2C766;
    font-family: 'Noto Sans KR', sans-serif;
    /*배경 색깔 고민 중...*/
    /*background-color: #6567A8;*/
  }

  .login-btn {
    }

  .layout-box {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 5vw;
  }

  .yo-img1 {
    height: 5vw;
    position: relative;
    top: 0.5vw;
    -webkit-animation:yo-img1 1s infinite;
    -moz-animation:yo-img1 1s infinite;
    animation:yo-img1 1s infinite;
  }

  @-webkit-keyframes yo-img1{
      0% {opacity:0;}
      100% {opacity:1;}
  }
  @-moz-keyframes yo-img1{
      0% {opacity:0;}
      100% {opacity:1;}
  }
  @keyframes yo-img1{
      0% {opacity:0;}
      100% {opacity:1;}
  }

  .yo-img2 {
    height: 5vw;
    position: relative;
    right: 5.3vw;
    top: 0.6vw;
    -webkit-animation:yo-img2 1s infinite;
    -moz-animation:yo-img2 1s infinite;
    animation:yo-img2 1s infinite;
  }

  @-webkit-keyframes yo-img2{
      0% {opacity:1;}
      100% {opacity:0;}
  }
  @-moz-keyframes yo-img2{
      0% {opacity:1;}
      100% {opacity:0;}
  }
  @keyframes yo-img2{
      0% {opacity:1;}
      100% {opacity:0;}
  }
</style>