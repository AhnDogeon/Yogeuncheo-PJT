<template>
  <v-form ref="form">
    <v-layout justify-center class="main-description1">
      이사할 곳이
      <span class="main-description2">
        어떤 동네
      </span>
      인지 궁금한가요?
    </v-layout>


      <v-row class="justify-center" style="margin-top: 2vw;">
        <v-col class="col-9 col-md-5 text1" style="margin-left: 2.5vw;">
          <v-text-field color="v-label" v-model="searchAddress" label="서울특별시 OO구 OO동을 정확히 입력하세요" @keypress.enter.prevent="onSubmit" outlined/>
        </v-col>
        <v-col class="col-1" style="margin-left: -2vw;">
          <v-btn text icon @click.stop="onSubmit">
        <v-icon class="mdi">mdi-magnify</v-icon>
      </v-btn>
        </v-col>
      </v-row>



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
                console.log("search : " + this.$store.state.data.dong2.address);
                this.initScore();
                this.getScoreOfDong(params);
            },
          async initScore() {
            console.log("initScore");
            const params = { dong2 : { address : "" }};

            console.log("search2 : " + this.$store.state.data.dong2.address);
            this.$store.commit("data/initDong2", params.dong2);
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

  @media screen and (max-width: 767px) {
    .main-description1 {
      font-family: 'Noto Sans KR', sans-serif;
      font-weight: 700;
      font-size: 18px;
      margin-top: 2vh;
      margin-left: 1vw;
    }
  }

  .main-description2 {
    color: #6567A8;
    margin-left: 0.8vw;
  }

  .mdi {
    font-size: 2vw !important;
  }

  @media screen and (max-width: 767px) {
    .mdi {
      font-size: 20px !important;
    }
  }
</style>