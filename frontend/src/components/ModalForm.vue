<template>
  <v-dialog
    v-model="dialog"
    max-width="40vw"
  >
    <v-card>
      <v-card-title class="title1">강남구 역삼동 <span class="title2"> 은 이런 동네예요 😊</span></v-card-title>

      <v-card-text>
        아래의 지수는 강남구 역삼동에 대한 정보입니다. <br>
        편의시설, 범죄율, 공공기관 빅데이터를 이용해 표준 지수로 변환해 정보를 제공합니다.
      </v-card-text>

      <v-container>
        <v-row dense>
            <v-layout class="circle1">
              편의시설 80점
            </v-layout>
            <v-layout class="circle2 mx-3">
              물가지수 60점
            </v-layout>

            <v-layout class="circle3">
              범죄율 23%
            </v-layout>
        </v-row>
      </v-container>


      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn
          color="green darken-1"
          text
          @click="emitValue"
        >
          닫기
        </v-btn>

        <v-btn
          color="green darken-1"
          text
          @click="goMaps()"
        >
          자세히 보러 가기
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
    export default {
        name: 'ModalForm',
        props: {
            dialogOpen: {type: Boolean}
        },
        data() {
            return {
                dialog: false,
            }
        },
        methods: {
            emitValue() {
                this.dialog = false
                this.$emit('dialogClose');
            },
            goMaps() {
                this.$router.push('/maps');
            }
        },
        mounted() {
        },
        watch: {
            dialogOpen: function (val) {
                if (val) {
                    this.dialog = true
                }
            },
            dialog: function (val) {
                if (val === false) {
                    this.emitValue()
                }
            },
        },
        computed: {}
    }
</script>

<style>
  .title1 {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    color: #6567A8;
  }

  .title2 {
    font-weight: 500;
    color: black;
  }

  .circle1 {
    width: 1vw;
    height: 24vh;
    border-radius: 50%;
    background-color: #5d76b9;
    font-size: 1.2vw;
    justify-content: center;
    line-height: 24vh;
    color: black;
    font-weight: 500;
  }

  .circle2 {
    width: 1vw;
    height: 24vh;
    border-radius: 50%;
    background-color: #e7ca58;
    font-size: 1.2vw;
    justify-content: center;
    line-height: 24vh;
    color: black;
    font-weight: 500;
  }

  .circle3 {
    width: 1vw;
    height: 24vh;
    border-radius: 50%;
    background-color: #d46f1a;
    font-size: 1.2vw;
    justify-content: center;
    line-height: 24vh;
    color: black;
    font-weight: 500;
  }
</style>