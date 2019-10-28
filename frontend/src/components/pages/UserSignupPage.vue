<template>
  <v-container>
    <v-layout row>
      <v-col cols="6">
        <v-text-field v-model="username" label="ID"/> <v-btn @click="check">중복검사</v-btn>
        <v-text-field v-model="password" :type="'password'" label="Password"/>
        <v-text-field v-model="gender" label="Gender"/>
        <v-text-field v-model="age" label="Age"/>
        <v-text-field v-model="occupation" label="Occupation"/>
      </v-col>
    </v-layout>
    <v-layout>
      <v-btn @click="signup">회원가입</v-btn>
    </v-layout>
  </v-container>
</template>

<script>
    import api from '../../api'

    export default {
        name: "UserSignupPage",
        data: () => ({
            username: '',
            password: '',
            gender: '',
            age: '',
            occupation: '',
        }),
        methods: {
            signup: async function () {
                const info =
                    {
                        "username": this.username,
                        "password": this.password,
                        "gender": this.gender,
                        "age": this.age,
                        "occupation": this.occupation
                    }
                ;
                const resp = await api.signup(info);
                if (resp.status === 201) {
                    const resp = await api.login(info);
                    const auth = resp.data;
                    if (auth.status) {
                        this.$store.commit('data/login',auth.user);
                    }
                    this.$store.state.authDialog = false;
                    this.username = '';
                    this.password = '';
                    this.gender = '';
                    this.age = '';
                    this.occupation = '';
                } else {
                    //TODO: 회원가입 실패시 실패 메시지 => 어떤 이유로 실패했는지
                    console.log("회원가입 실패")
                }
            },
            check: async function() {
                const info = { 'username': this.username };
                const resp = await api.checkIsDuplicated(info);
                if (resp.data.isDuplicated) {
                    //TODO: ID가 중복이라고 표시
                    alert('중복된 아이디입니다.')
                    console.log('중복된 아이디입니다')
                } else {
                    //TODO: 사용 가능한 ID 표시
                    alert('사용 가능한 아이디입니다.')
                    console.log('노 중복')
                }
            },

        },
    }
</script>

<style scoped>

</style>