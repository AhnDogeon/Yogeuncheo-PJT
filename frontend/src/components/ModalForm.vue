<template>
  <v-dialog
      v-model="dialog"
      width="1000px"
  >
    <v-card>
      <v-card-title><p class="main-title">{{oneDong.address}} <span class="title2"> 은 이런 동네예요 😊</span></p>
      </v-card-title>

      <v-card-text>
        <p class="main-text">
          아래의 지수는 {{oneDong.address}}에 대한 정보입니다. <br>
          편의시설, 공원 분포, 학교 비율, 범죄율 등의 빅데이터를 표준 지수로 변환해 정보를 제공합니다.
        </p>

      </v-card-text>

      <v-container>
        <v-row dense>
          <v-col class="col-12 col-md-2">
            <v-row class="info1 col-12">
              <span class="info-title">편의지수</span>
              <img src="../assets/store.png" alt="store" class="info-img">
              <span class="qs">? <span class="popover">편의지수는 각 동의 프랜차이즈, 편의점, 영화관의 매장 수에 자체 알고리즘을 적용해 환산한 점수입니다. <p
                  style="color: #dc3240">매달 업데이트 됩니다.</p></span></span>
            </v-row>
            <p class="co1-12" v-if="oneDong.total_score <= 10" style="color: #ff3a29; text-align: center; font-size: 20px; font-weight: 600; margin-top: 10px;">낮음</p>
            <p class="co1-12" v-else-if="oneDong.total_score <= 45" style="color: #ff8f0e; text-align: center; font-size: 20px; font-weight: 600; margin-top: 10px;">평균</p>
            <p class="co1-12" v-else-if="46 <= oneDong.total_score" style="color: #025523; text-align: center; font-size: 20px; font-weight: 600; margin-top: 10px;">높음</p>
            <p class="co1-12" style="font-size: 18px; font-weight: 600; margin: auto; text-align: center;">
              {{oneDong.total_score}}점
            </p>
          </v-col>
          <v-col class="col-12 col-md-2">
            <v-row class="info1 col-12">
              <span class="info-title">숲세권</span>
              <img src="../assets/forest.png" alt="forest" class="info-img">
              <span class="qs">? <span class="popover">공원지수는 0~5개는 낮음, 6~15개는 보통, 그 이상은 쾌적입니다.  <p
                  style="color: #dc3240">매년 업데이트 됩니다.</p></span></span>
            </v-row>
            <v-row class="col-12">
              <div v-if="oneDong.park_count <= 5" class="info-text">
                <p style="color: #ff3a29; text-align: center; font-size: 20px; font-weight: 600;">낮음</p>
                <p>총 : {{oneDong.park_count}}개</p>
              </div>
              <div v-else-if="oneDong.park_count <= 15" class="info-text">
                <p style="color: #ff8f0e; text-align: center; font-size: 20px; font-weight: 600;">보통</p>
                <p>총 : {{oneDong.park_count}}개</p>
              </div>
              <div v-else-if="16 <= oneDong.park_count" class="info-text">
                <p style="color: #025523; text-align: center; font-size: 20px; font-weight: 600;">쾌적</p>
                <p>총 : {{oneDong.park_count}}개</p>
              </div>
            </v-row>
          </v-col>
          <v-col class="col-12 col-md-2">
            <v-row class="info1 col-12">
              <span class="info-title">교육지수</span>
              <img src="../assets/school.png" alt="school" class="info-img">
              <span class="qs">? <span class="popover">교육지수는 각 동의 초등학교, 중학교, 고등학교 합을 나타내며 0~10개는 낮음, 11~20개는 보통, 그 이상은 높음입니다.  <p
                  style="color: #dc3240">매년 업데이트 됩니다.</p></span></span>
            </v-row>
            <v-row class="col-12">
              <div v-if="oneDong.elementary_count + oneDong.middle_count + oneDong.high_count <= 10"
                   class="info-text">
                <p style="color: #ff3a29; text-align: center; font-size: 20px; font-weight: 600;">낮음</p>
                <p>초등학교 : {{ oneDong.elementary_count }}개</p>
                <p>중학교 : {{ oneDong.middle_count }}개</p>
                <p>고등학교 : {{ oneDong.high_count }}개</p>
              </div>
              <div v-else-if="oneDong.elementary_count + oneDong.middle_count + oneDong.high_count <= 20"
                   class="info-text">
                <p style="color: #ff6a07; text-align: center; font-size: 20px; font-weight: 600;">보통</p>
                <p>초등학교 : {{ oneDong.elementary_count }}개</p>
                <p>중학교 : {{ oneDong.middle_count }}개</p>
                <p>고등학교 : {{ oneDong.high_count }}개</p>
              </div>
              <div v-if="21 <= oneDong.elementary_count + oneDong.middle_count + oneDong.high_count"
                   class="info-text">
                <p style="color: #025523; text-align: center; font-size: 20px; font-weight: 600;">높음</p>
                <p>초등학교 : {{ oneDong.elementary_count }}개</p>
                <p>중학교 : {{ oneDong.middle_count }}개</p>
                <p>고등학교 : {{ oneDong.high_count }}개</p>
              </div>
            </v-row>
          </v-col>
          <v-col class="col-12 col-md-3">
            <v-row class="info1 col-12">
              <span class="info-title">유가지수</span>
              <img src="../assets/gas.png" alt="gas" class="info-img">
              <span class="qs">? <span class="popover">유가지수는 각 동 주유소의 고급휘발유, 휘발유, 경유의 평균 가격 입니다.  <p
                  style="color: #dc3240">매주 업데이트 됩니다.</p></span></span>
            </v-row>
            <v-row class="col-12" style="text-align: center; font-size: 16px;">
              <p class="col-12" style="margin: 0;">고급 휘발유 : {{oneDong.high_oil}}원</p>
              <p class="col-12" style="margin: 0">휘발유 : {{oneDong.oil}}원</p>
              <p class="col-12" style="margin: 0">경유 : {{oneDong.oil2}}원</p>
            </v-row>
          </v-col>
          <v-col class="col-12 col-md-3">
            <v-row class="info1 col-12">
              <span class="info-title">안전지수</span>
              <img src="../assets/police.jpg" alt="police" class="info-img">
              <span class="qs">? <span class="popover" style="left:-45px;">안전지수는 각 동 범죄 발생건수, 검거건수를 바탕으로 검거율을 계산합니다.  <p
                  style="color: #dc3240">매년 업데이트 됩니다.</p></span></span>
            </v-row>
            <v-row class="col-12" style="text-align: center; font-size: 16px;">
              <p class="col-12" style="font-size: 20px; font-weight: 600; margin: auto 0;">검거율 :
                {{oneDong.percent}}%</p>
              <p class="col-12" style="margin: 0;">발생건수 : {{oneDong.total}}건</p>
              <p class="col-12" style="margin: 0;">검거건수 : {{oneDong.catch}}건</p>
            </v-row>
          </v-col>
        </v-row>
      </v-container>


      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" text @click="emitValue">닫기</v-btn>
        <v-btn color="green darken-1" text @click="goMaps()">자세히 보러 가기</v-btn>
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
  .main-title {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    color: #6567A8;
    font-size: 24px;
  }

  @media screen and (max-width: 767px) {
    .main-title {
      font-size: 18px;
    }
  }

  .title2 {
    font-weight: 500;
    color: black;
    font-size: 22px;
  }

  @media screen and (max-width: 767px) {
    .title2 {
      font-size: 14px;
    }
  }

  .main-text {
    font-size: 14px;
  }

  @media screen and (max-width: 767px) {
    .main-text {
      font-size: 12px;
    }
  }

  .info1 {
    margin: auto;
    justify-content: center;
    font-family: 'Noto Sans KR', sans-serif;
  }

  .info-img {
    width: 20px;
    height: 20px;
    margin-top: 3px;
  }

  .info-title {
    font-size: 20px;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    color: #008cbf;
    margin: auto 0.5vw;
  }

  /* The element to hover over */
  .qs {
    background-color: #858380;
    border-radius: 18px;
    color: #ffffff;
    cursor: default;
    display: inline-block;
    font-family: 'Helvetica', sans-serif;
    font-size: 15px;
    font-weight: bold;
    height: 18px;
    width: 18px;;
    line-height: 18px;
    position: relative;
    text-align: center;
    left: 5px;
    top: 5px;
  }

  .qs .popover {
    background-color: #ffdf6c;
    border-radius: 5px;
    color: #000000;
    display: none;
    font-size: 12px;
    font-family: 'Noto Sans KR', sans-serif;
    padding: 5px;
    position: absolute;
    width: 125px;
    height: 135px;
    top: 10px;
    z-index: 4;
    left: 8px;
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

  .info-text {
    font-size: 16px;
    margin: auto;
  }

</style>