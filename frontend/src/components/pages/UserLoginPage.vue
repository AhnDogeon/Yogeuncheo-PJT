<template>
  <v-container>
    <v-layout row>
      <v-col cols="6">
        <v-text-field v-model="username" label="ID"/>
        <v-text-field v-model="password" :type="'password'" label="Password"/>
      </v-col>
    </v-layout>
    <v-layout>
      <v-btn @click="login">로그인</v-btn>
    </v-layout>
  </v-container>
</template>

<script>
    import api from '../../api'

    export default {
        name: "UserLoginPage",
        data: () => ({
            username: '',
            password: '',
        }),
        methods: {
            login: async function () {
                const info = {
                    "username": this.username,
                    "password": this.password,
                };
                const resp = await api.login(info);
                const auth = resp.data;
                if (auth.status) {
                    this.$store.commit('data/login', auth.user);
                    this.username = '';
                    this.password = '';
                    this.$store.state.authDialog = false
                } else {
                    //TODO: msg="아이디 또는 비밀번호를 확인해주세요"
                }
            },
        },
    }
</script>

<style scoped>

</style>