<template>
  <v-dialog
      v-model="dialog"
      width="700px"
  >
    <v-card>
      <v-card-title style="font-family: 'Noto Sans KR', sans-serif; font-weight: 700; color: #6567A8; font-size: 1.4vw;">{{oneDong.address}} <span class="title2"> 은 이런 동네예요 😊</span></v-card-title>

      <v-card-text style="font-size: 1vw;">
        아래의 지수는 {{oneDong.address}}에 대한 정보입니다. <br>
        편의시설, 범죄율, 공공기관의 빅데이터를 표준 지수로 변환해 정보를 제공합니다.
      </v-card-text>

      <v-container>
        <v-row dense>
          <v-col>
            <v-row class="info1">
              <span class="info-title">편의지수</span>
              <img src="../assets/store.png" alt="store" class="info-img">
              <div class="center">
                <span class="qs">? <span class="popover above" style="left: -3vw;">편의지수는 각 동의 프랜차이즈, 편의점, 영화관의 매장 수에 자체 알고리즘을 적용해 환산한 점수입니다. <p style="color: #dc3240">매달 업데이트 됩니다.</p></span></span>
              </div>
            </v-row>
            <p style="font-size: 1.3vw; font-family: 'Noto Sans KR', sans-serif; font-weight: 600; margin-top: 2vw; margin-left: 3vw;">
              {{oneDong.total_score}}점</p>
          </v-col>
          <v-col>
            <v-row class="info1">
              <span class="info-title">유가지수</span>
              <img src="../assets/gas.png" alt="gas" class="info-img">
              <div class="center">
                <span class="qs">? <span class="popover above" style="height: 6vw;">유가지수는 각 동 주유소의 고급휘발유, 휘발유, 경유의 평균 가격 입니다.  <p style="color: #dc3240">매주 업데이트 됩니다.</p></span></span>
              </div>
            </v-row>
            <v-row style="margin-left: 1vw; margin-top: 1vw; font-size: 1.1vw;">
              <p>고급 휘발유 : {{oneDong.high_oil}}원</p>
              <p>휘발유 : {{oneDong.oil}}원</p>
              <p>경유 : {{oneDong.oil2}}원</p>
            </v-row>

          </v-col>

          <v-col>
            <v-row class="info1">
              <span class="info-title">안전지수</span>
              <img src="../assets/police.jpg" alt="police" class="info-img">
              <div class="center">
                <span class="qs">? <span class="popover above" style="height: 6.5vw; left: -9vw;">안전지수는 각 동 범죄 발생건수, 검거건수를 바탕으로 검거율을 계산합니다.  <p style="color: #dc3240">매년 업데이트 됩니다.</p></span></span>
              </div>
            </v-row>
            <v-row style="margin-left: 1vw; margin-top: 1vw; font-size: 1vw;">
              <p style="font-size: 1.3vw; font-weight: 600;">검거율 : {{oneDong.percent}}%</p>
              <p>발생건수 : {{oneDong.total}}건</p>
              <p>검거건수 : {{oneDong.catch}}건</p>
            </v-row>


          </v-col>
        </v-row>
      </v-container>


      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn
            color="green darken-1"
            text
            @click="emitValue"
            style="font-size: 1vw;"
        >
          닫기
        </v-btn>

        <v-btn
            color="green darken-1"
            text
            @click="goMaps()"
            style="font-size: 1vw;"
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
        computed: {
            oneDong: function () {
                return this.$store.state.data.dong_info
            }
        }
    }
</script>

<style>
  .title2 {
    font-weight: 500;
    color: black;
    font-size: 1.4vw;
  }

  .info1 {
    margin: auto;
    justify-content: center;
  }

  .info-img {
    width: 2.5vw;
    height: 2.5vw;
  }

  .info-title {
    font-size: 1.5vw;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    color: #008cbf;
    margin: auto 0.5vw;
  }

  /* The element to hover over */
  .qs {
    background-color: #858380;
    border-radius: 1.5vw;
    color: #ffffff;
    cursor: default;
    display: inline-block;
    font-family: 'Helvetica', sans-serif;
    font-size: 1.1vw;
    font-weight: bold;
    height: 1.4vw;
    line-height: 1.4vw;
    position: relative;
    text-align: center;
    width: 1.4vw;
    left: 0.4vw;
    top: 0.3vw;
  }

  .qs .popover {
    background-color: #ffdf6c;
    border-radius: 0.2vw;
    color: #000000;
    display: none;
    font-size: 0.8vw;
    font-family: 'Noto Sans KR', sans-serif;
    padding: 0.4vw;
    position: absolute;
    width: 10vw;
    height: 8vw;
    top: 2vw;
    z-index: 4;
  }

  .qs:hover .popover {
    display: block;
    -webkit-animation: fade-in .3s linear 1, move-up .3s linear 1;
    -moz-animation: fade-in .3s linear 1, move-up .3s linear 1;
    -ms-animation: fade-in .3s linear 1, move-up .3s linear 1;
  }

  @-webkit-keyframes fade-in {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @-moz-keyframes fade-in {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @-ms-keyframes fade-in {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @-webkit-keyframes move-up {
    from {
      bottom: 30px;
    }
    to {
      bottom: 42px;
    }
  }

  @-moz-keyframes move-up {
    from {
      bottom: 30px;
    }
    to {
      bottom: 42px;
    }
  }

  @-ms-keyframes move-up {
    from {
      bottom: 30px;
    }
    to {
      bottom: 42px;
    }
  }

</style>