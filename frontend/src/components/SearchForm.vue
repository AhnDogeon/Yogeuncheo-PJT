<template>
  <v-form ref="form">
    <v-layout justify-center class="main-description1">
      이사할 곳이
      <span class="main-description2">
        어떤 동네
      </span>
      인지 궁금한가요?
    </v-layout>


    <v-layout class="search-form">
      <v-text-field color="v-label" v-model="searchAddress" label="OO구 OO동을 검색해보세요" outlined/>
      <v-btn text icon @click.stop="onSubmit">
        <v-icon class="mdi">mdi-magnify</v-icon>
      </v-btn>
    </v-layout>
    <ModalForm v-on:dialogClose="dialogClose" :dialogOpen="dialogOpen"></ModalForm>
  </v-form>
</template>

<script>
    import ModalForm from '@/components/ModalForm'
    import {mapActions} from 'vuex';

    export default {
        props: {
        },
        components: {
            ModalForm,
        },
        data: () => ({
            searchAddress: "",
            dialogOpen: false,

        }),
        methods: {
            ...mapActions("data", ["getScoreOfDong"]),
            onSubmit: function () {
                this.dialogOpen = true
                const params = {
                    searchAddress: this.searchAddress,
                };
                this.getScoreOfDong(params);
            },
            dialogClose() {
                this.dialogOpen = false
            }
        },
    };
</script>

<style scoped>
  .main-description1 {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    font-size: 2vw;
    margin-top: 2vh;
    margin-left: 1vw;
  }

  .main-description2 {
    color: #6567A8;
    margin-left: 0.8vw;
  }

  .search-form {
    width: 28vw;
    margin: 8vh auto 0;
  }

  .v-label {
    font-size: 1vw !important;
  }

  .v-input__slot {
    width: 2vw !important;
    height: 5vh !important;
  }

  .mdi {
    font-size: 2vw !important;
  }
</style>