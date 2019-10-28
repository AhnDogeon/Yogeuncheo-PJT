<template>
  <v-card>
    <v-tabs v-model="tab">
      <v-tabs-slider />
      <v-tab>로그인</v-tab>
      <v-tab>회원가입</v-tab>
      <v-spacer></v-spacer>
      <v-btn @click="close">닫기</v-btn>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-card>
          <v-card-text>
            <UserLoginPage />
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card>
          <v-card-text>
            <UserSignupPage />
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
    import UserSignupPage from "../pages/UserSignupPage"
    import UserLoginPage from "../pages/UserLoginPage"

    export default {
        name: "UserAuth",
        components: {
          UserSignupPage,
          UserLoginPage
        },
        data: () => ({
            tab: null,
        }),
        methods: {
            close() {
                this.$store.state.authDialog = false
            }
        }
    }
</script>

<style scoped>

</style>