<template>
  <v-content>
    <v-layout justify-center class="main-description1">
      지도를 클릭해서
      <span class="main-description2">
        가고 싶은 동네의
      </span>
      자세한 점수를 확인해보세요!
    </v-layout>

    <v-row class="seoul-maps" dense>

      <v-col id="map" style="width:40vw; height:40vw;"></v-col>
      <v-col>
        <v-row>
          <v-layout v-if="dong2_name">
            <div>
              <v-select style="width: 12vw; margin-left: 2vw;" v-model="selected_dong" :label="dong2_name"
                        :items="dong_list" item-color="blue-grey lighten-5" outlined></v-select>
            </div>
            <div>
              <v-icon style="margin-left: 0.8vw; margin-top: 1vw; font-size: 1.5vw;" @click="getScore">mdi-magnify
              </v-icon>
            </div>
          </v-layout>

          <v-layout v-else="dong_origin">
            <div>
              <v-select style="width: 12vw; margin-left: 2vw;" v-model="dong_origin_name" :label="dong_origin.gu"
                        :items="dong_origin.dong" item-color="blue-grey lighten-5" outlined return-object></v-select>
            </div>
            <div>
              <v-icon style="margin-left: 0.8vw; margin-top: 1vw; font-size: 1.5vw;" @click="getScore">mdi-magnify
              </v-icon>
            </div>
          </v-layout>
        </v-row>
        <v-row>
          <v-layout v-if="dong2_name">
            {{dong2.mac_score}}
            <br>
            {{dong2.total_score}}
          </v-layout>
          <v-layout v-else="dong_origin">
            {{dong_origin.total_score}}
          </v-layout>
        </v-row>
      </v-col>
    </v-row>


    ​
    ​
    <!--<div class="waves1"></div>-->
    <!--<div class="waves2"></div>-->
    <!--<div class="waves3"></div>-->
    ​
  </v-content>
</template>
​
<script>
    import seoul_coor from '../../assets/seoul';
    import {mapActions} from 'vuex';

    export default {
        data: () => ({
            isImgTrue: false,
            selected_dong: '',
            dong2_name: '',
            dong_origin_name: '',
        }),

        methods: {
            ...mapActions("data", ["getListOfDong", "getDong2"]),
            async onSubmit(name) {
                const params = {
                    gu: name,
                };
                await this.getListOfDong(params);
            },
            async getScore() {
                const params = {
                    dong2: this.selected_dong,
                };
                await this.getDong2(params);
            }
        },
        computed: {
            dong_list() {
                return this.$store.state.data.dong_list
            },
            dong2() {
                return this.$store.state.data.dong2
            },
            dong_origin() {
                this.dong_origin_name = this.$store.state.data.dong_info.dong;
                return this.$store.state.data.dong_info
            }
        }
        ,
        mounted: function () {
            var mapContainer = document.getElementById('map'), // 지도를 표시할 div
                mapOption = {
                    center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
                    level: 9 // 지도의 확대 레벨
                };
            var map = new kakao.maps.Map(mapContainer, mapOption),
                customOverlay = new kakao.maps.CustomOverlay({}),
                infowindow = new kakao.maps.InfoWindow({removable: true});
            var seoul_co = seoul_coor.features;
            var coordinates = [];
            var name = '';
            var polygons = [];
            seoul_co.forEach(val => {
                coordinates = val.geometry.coordinates;
                name = val.properties.SIG_KOR_NM;
                displayPolygon(coordinates, name, this);
            });

            function displayPolygon(coordinates, name, vueInstance) {
                var path = [];
                var points = [];
                coordinates[0].forEach(coordinate => {
                    var point = new Object();
                    point.x = coordinate[1];
                    point.y = coordinate[0];
                    points.push(point);
                    path.push(new kakao.maps.LatLng(coordinate[1], coordinate[0]));
                });
                var polygon = new kakao.maps.Polygon({
                    map: map, // 다각형을 표시할 지도 객체
                    path: path,
                    strokeWeight: 2,
                    strokeColor: '#004c80',
                    strokeOpacity: 0.8,
                    fillColor: '#fff',
                    fillOpacity: 0.7
                });
                // 다각형에 mouseover 이벤트를 등록하고 이벤트가 발생하면 폴리곤의 채움색을 변경합니다
                // 지역명을 표시하는 커스텀오버레이를 지도위에 표시합니다
                kakao.maps.event.addListener(polygon, 'mouseover', function (mouseEvent) {
                    polygon.setOptions({fillColor: '#09f'});
                    customOverlay.setContent('<div class="area">' + name + '</div>');
                    //
                    customOverlay.setPosition(mouseEvent.latLng);
                    customOverlay.setMap(map);
                });
                // 다각형에 mousemove 이벤트를 등록하고 이벤트가 발생하면 커스텀 오버레이의 위치를 변경합니다
                kakao.maps.event.addListener(polygon, 'mousemove', function (mouseEvent) {
                    customOverlay.setPosition(mouseEvent.latLng);
                });
                // 다각형에 mouseout 이벤트를 등록하고 이벤트가 발생하면 폴리곤의 채움색을 원래색으로 변경합니다
                // 커스텀 오버레이를 지도에서 제거합니다
                kakao.maps.event.addListener(polygon, 'mouseout', function () {
                    polygon.setOptions({fillColor: '#fff'});
                    customOverlay.setMap(null);
                });
                kakao.maps.event.addListener(polygon, 'click', () => {
                    vueInstance.dong_list = vueInstance.onSubmit(name);
                    vueInstance.dong2_name = name;
                });
                polygons.push(polygon);
            }
        },
    }
</script>

<style>
  .seoul-maps {
    margin-top: 2vw;
  }

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
    margin-right: 0.5vw;
  }

  .v-label {
    font-size: 1vw !important;
  }

  .v-select__selection {
    font-size: 1.2vw !important;
  }

  /*wave 애니메이션 */
  .waves1 {
    position: absolute;
    left: 20vw;
    top: 28vh;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    background: rgba(255, 129, 109, 0.4);
    width: 25px;
    height: 25px;
    border-radius: 50%;
  }

  .waves1:before, .waves1:after {
    content: "";
    position: absolute;
    background: #ff5456;
    margin-left: -12px;
    margin-top: -12px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    -webkit-animation: wave1 3s infinite linear;
    animation: wave1 3s infinite linear;
  }

  .waves1:after {
    opacity: 0;
    -webkit-animation: wave1 3s 1.5s infinite linear;
    animation: wave1 3s 1.5s infinite linear;
  }

  @-webkit-keyframes wave1 {
    0% {
      -webkit-transform: scale(0);
      transform: scale(0);
      opacity: 1;
    }
    100% {
      -webkit-transform: scale(2);
      transform: scale(2);
      opacity: 0;
    }
  }


  @keyframes wave1 {
    0% {
      -webkit-transform: scale(0);
      transform: scale(0);
      opacity: 1;
    }
    100% {
      -webkit-transform: scale(2);
      transform: scale(2);
      opacity: 0;
    }
  }

  /*wave2 애니메이션 */
  .waves2 {
    position: absolute;
    left: 12vw;
    top: 50vh;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    background: rgba(35, 36, 255, 0.4);
    width: 25px;
    height: 25px;
    border-radius: 50%;
  }

  .waves2:before, .waves2:after {
    content: "";
    position: absolute;
    background: #7fa7ff;
    margin-left: -12px;
    margin-top: -12px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    -webkit-animation: wave2 3s infinite linear;
    animation: wave2 3s infinite linear;
  }

  .waves2:after {
    opacity: 0;
    -webkit-animation: wave2 3s 1.5s infinite linear;
    animation: wave2 3s 1.5s infinite linear;
  }

  @-webkit-keyframes wave2 {
    0% {
      -webkit-transform: scale(0);
      transform: scale(0);
      opacity: 1;
    }
    100% {
      -webkit-transform: scale(2);
      transform: scale(2);
      opacity: 0;
    }
  }


  @keyframes wave2 {
    0% {
      -webkit-transform: scale(0);
      transform: scale(0);
      opacity: 1;
    }
    100% {
      -webkit-transform: scale(2);
      transform: scale(2);
      opacity: 0;
    }
  }

  /*wave3 애니메이션 */
  .waves3 {
    position: absolute;
    left: 30vw;
    top: 55vh;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    background: rgba(255, 226, 59, 0.4);
    width: 25px;
    height: 25px;
    border-radius: 50%;
  }

  .waves3:before, .waves3:after {
    content: "";
    position: absolute;
    background: #ff983d;
    margin-left: -12px;
    margin-top: -12px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    -webkit-animation: wave3 3s infinite linear;
    animation: wave3 3s infinite linear;
  }

  .waves3:after {
    opacity: 0;
    -webkit-animation: wave3 3s 1.5s infinite linear;
    animation: wave3 3s 1.5s infinite linear;
  }


  @-webkit-keyframes wave3 {
    0% {
      -webkit-transform: scale(0);
      transform: scale(0);
      opacity: 1;
    }
    100% {
      -webkit-transform: scale(2);
      transform: scale(2);
      opacity: 0;
    }
  }


  @keyframes wave3 {
    0% {
      -webkit-transform: scale(0);
      transform: scale(0);
      opacity: 1;
    }
    100% {
      -webkit-transform: scale(2);
      transform: scale(2);
      opacity: 0;
    }
  }

  .area {
    position: absolute;
    background: #fff;
    border: 1px solid #888;
    border-radius: 3px;
    font-size: 12px;
    top: -5px;
    left: 15px;
    padding: 2px;
  }
</style>