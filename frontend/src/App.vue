<template>
  <v-app id="app">
    <v-container class="container-box">
      <!--<v-layout justify-end class="login-btn">-->
<!--        <v-dialog v-model="$store.state.authDialog">-->
<!--          <template v-slot:activator="{ on }">-->
<!--&lt;!&ndash;            <v-btn text v-on="on">&ndash;&gt;-->
<!--&lt;!&ndash;              로그인&ndash;&gt;-->
<!--&lt;!&ndash;            </v-btn>&ndash;&gt;-->
<!--            <div v-if="access_token">-->
<!--              <v-btn>로그아웃</v-btn>-->
<!--            </div>-->
<!--            <div v-else>-->
<!--              <KakaoLogin-->
<!--                api-key="cea5b8ae3384be46febd687ef54537dc"-->
<!--                image="kakao_login_btn_small"-->
<!--                :on-success=onSuccess-->
<!--                :on-failure=onFailure-->
<!--              />-->
<!--            </div>-->
<!--          </template>-->
<!--        </v-dialog>-->
      <!--</v-layout>-->
      <router-link :to="{name: 'home'}" style="text-decoration: none; color: black;">
        <v-layout class="layout-box" justify-center style="margin-top: 5vh;">
          <p style="margin-left: 8vw;">
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
  import router from './router';
  import KakaoLogin from 'vue-kakao-login'

  let onSuccess = (data) => {
        console.log(data.access_token);
        // console.log(this.access_token);
        // this.access_token=data.access_token;
        // console.log(this.access_token);
        console.log("success")
    }
  let onFailure = (data) => {
      console.log(data)
      console.log("failure")
  }

  export default {
        components: {
            KakaoLogin
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
            access_token: '',
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
            onSuccess,
            onFailure,
        }
    };
</script>

<style>
    #app {
    background-color: #f2c766;
    font-family: 'Noto Sans KR', sans-serif;
  }


  .layout-box {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 5vw;
    margin-top: ;
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