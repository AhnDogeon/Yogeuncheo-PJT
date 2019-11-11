<template>
  <v-content>
    <v-layout justify-center class="main-description1">
      지도를 클릭해서
      <span class="main-description2">
        원하는 동네의
      </span>
      자세한 정보를 확인해보세요!
    </v-layout>
    <v-row class="seoul-maps" dense>
      <v-col class="col-md-6 col-12" id="map"></v-col>
      <v-col class="col-md-6 col-12">
        <v-col class="col-12">
            <v-layout v-if="dong2_name">
              <v-select class="col-10 col-md-7" v-model="selected_dong" :label="dong2_name"
                        :items="dong_list" item-color="blue-grey lighten-5" outlined></v-select>
              <v-icon class="col-2" style="margin-bottom: 20px; margin-left:-15px; font-size: 30px;" @click="getScore">mdi-magnify</v-icon>
            </v-layout>
            <v-layout v-else="dong_origin">
              <v-select class="col-10 col-md-7" v-model="dong_origin_name" :label="dong_origin.gu"
                        :items="dong_origin.dong" item-color="blue-grey lighten-5" outlined></v-select>
              <v-icon class="col-2" style="margin-bottom: 20px; margin-left:-15px; font-size: 30px;" @click="getScore">mdi-magnify</v-icon>
            </v-layout>
        </v-col>
        <v-col class="col-12">
          <div v-if="dong2_name" class="map-description">
            <p style="font-size: 20px; font-weight: 700; color: #6567A8;">{{ dong2.address }}<span
                style="color: black;">의 정보 입니다.</span></p>
            <p style="font-size: 20px; font-weight: 700; color: #a82a1a;">추천 동네 :<span style="margin-left:1vw; color: black">{{ dong2.first }}, {{ dong2.second }}, {{ dong2.third }}</span></p>
            <p style="font-size: 20px; font-weight: 700; color: #a82a1a;">역세권 :
              <span style="margin-left:1vw; color: black">{{ dong2.station }}</span>
            </p>
            <hr style="border-top: 1px solid black;">
            <p v-if="dong2.total_score <= 10" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              편의시설 {{ dong2.total_count }}개 <span style="color: #ff3a29; font-weight: 600;">적음</span>
            </p>
            <p v-else-if="dong2.total_score <= 45" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              편의시설 {{ dong2.total_count }}개 <span style="color: #ff6a07; font-weight: 600;">평균</span>
            </p>
            <p v-else-if="46 <= dong2.total_score" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              편의시설 {{ dong2.total_count }}개 <span style="color: #025523; font-weight: 600;">많음</span>
            </p>
            <v-row class="col-12" style="padding: 0;">
              <v-col>🍔 맥도날드 : {{ dong2.mac_count }}개</v-col>
              <v-col>🍟 롯데리아 : {{ dong2.lot_count }}개</v-col>
              <v-col>🥤 버거킹 : {{ dong2.burgerking_count }}개</v-col>
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>🏠 CU : {{ dong2.cu_count }}개</v-col>
              <v-col>🍱 gs25 : {{ dong2.gs25_count }}개</v-col>
              <v-col>🥡 세븐일레븐 : {{ dong2.seveneleven_count }}개</v-col>
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>☕ 스타벅스 : {{ dong2.starbucks_count }}개</v-col>
              <v-col>🎥 CGV : {{ dong2.cgv_count }}개</v-col>
              <v-col>🎞️ 메가박스 : {{ dong2.megabox_count }}개</v-col>
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>🍿 롯데시네마 : {{ dong2.lottecinema_count }}개</v-col>
            </v-row>
            <hr style="border-top: 1px solid black;">
            <p v-if="dong2.park_count <= 5" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              공원 {{ dong2.park_count }}개 <span style="color: #ff3a29; font-weight: 600;">낮음</span>
            </p>
            <p v-else-if="dong2.park_count <= 15" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              공원 {{ dong2.park_count }}개 <span style="color: #ff6a07; font-weight: 600;">보통</span>
            </p>
            <p v-else-if="16 <= dong2.park_count" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              공원 {{ dong2.park_count }}개 <span style="color: #025523; font-weight: 600;">쾌적</span>
            </p>
            <hr style="border-top: 1px solid black;">
            <v-row class="col-12" v-if="dong2.elementary_count + dong2.middle_count + dong2.high_count <= 10" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              교육지수 <span style="color: #ff3a29; font-weight: 600; margin-left: 5px;"> 낮음</span>
            </v-row>
            <v-row class="col-12" v-else-if="dong2.elementary_count + dong2.middle_count + dong2.high_count <= 20" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              교육지수 <span style="color: #ff6a07; font-weight: 600; margin-left: 5px;"> 보통</span>
            </v-row>
            <v-row class="col-12" v-else-if="21 <= dong2.elementary_count + dong2.middle_count + dong2.high_count" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              교육지수 <span style="color: #025523; font-weight: 600; margin-left: 5px;"> 높음</span>
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>초등학교 : {{ dong2.elementary_count }} 개</v-col>
              <v-col>중학교 : {{ dong2.middle_count }} 개</v-col>
              <v-col>고등학교 : {{ dong2.high_count }} 개</v-col>
            </v-row>
            <hr style="border-top: 1px solid black;">
            <v-row class="col-12" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              유가정보
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>고급 휘발유 : {{ dong2.high_oil }} 원</v-col>
              <v-col>휘발유 : {{ dong2.oil }} 원</v-col>
              <v-col>경유 : {{ dong2.oil2 }} 원</v-col>
            </v-row>
            <hr style="border-top: 1px solid black;">
            <v-row class="col-12" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              안전지수
            </v-row>
            <v-row style="margin-top: -0.9vw;">
              <v-col>발생건수 : {{ dong2.total }} 건</v-col>
              <v-col>검거건수 : {{ dong2.catch }} 건</v-col>
              <v-col>검거율 : {{ dong2.percent }} %</v-col>
            </v-row>
          </div>
          <div v-else-if="dong_origin" class="map-description">
            <p style="font-size: 20px; font-weight: 700; color: #6567A8;">{{ dong_origin.address }}<span
                style="color: black;">의 정보 입니다.</span></p>
            <p style="font-size: 20px; font-weight: 700; color: #a82a1a;">추천 동네 :<span style="margin-left:1vw; color: black">{{ dong_origin.first }}, {{ dong_origin.second }}, {{ dong_origin.third }}</span></p>
            <p style="font-size: 20px; font-weight: 700; color: #a82a1a;">역세권 :
              <span style="margin-left:1vw; color: black">{{ dong_origin.station }}</span>
            </p>
            <hr style="border-top: 1px solid black;">
            <p v-if="dong_origin.total_score <= 10" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              편의시설 {{ dong_origin.total_count }}개 <span style="color: #ff3a29; font-weight: 600;">적음</span>
            </p>
            <p v-else-if="dong_origin.total_score <= 45" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              편의시설 {{ dong_origin.total_count }}개 <span style="color: #ff6a07; font-weight: 600;">평균</span>
            </p>
            <p v-else-if="46 <= dong_origin.total_score" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              편의시설 {{ dong_origin.total_count }}개 <span style="color: #025523; font-weight: 600;">많음</span>
            </p>
            <v-row class="col-12" style="padding: 0;">
              <v-col>🍔 맥도날드 : {{ dong_origin.mac_count }}개</v-col>
              <v-col>🍟 롯데리아 : {{ dong_origin.lot_count }}개</v-col>
              <v-col>🥤 버거킹 : {{ dong_origin.burgerking_count }}개</v-col>
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>🏠 CU : {{ dong_origin.cu_count }}개</v-col>
              <v-col>🍱 gs25 : {{ dong_origin.gs25_count }}개</v-col>
              <v-col>🥡 세븐일레븐 : {{ dong_origin.seveneleven_count }}개</v-col>
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>☕ 스타벅스 : {{ dong_origin.starbucks_count }}개</v-col>
              <v-col>🎥 CGV : {{ dong_origin.cgv_count }}개</v-col>
              <v-col>🎞️ 메가박스 : {{ dong_origin.megabox_count }}개</v-col>
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>🍿 롯데시네마 : {{ dong_origin.lottecinema_count }}개</v-col>
            </v-row>
            <hr style="border-top: 1px solid black;">
            <p v-if="dong_origin.park_count <= 5" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              공원 {{ dong_origin.park_count }}개 <span style="color: #ff3a29; font-weight: 600;">낮음</span>
            </p>
            <p v-else-if="dong_origin.park_count <= 15" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              공원 {{ dong_origin.park_count }}개 <span style="color: #ff6a07; font-weight: 600;">보통</span>
            </p>
            <p v-else-if="16 <= dong_origin.park_count" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              공원 {{ dong_origin.park_count }}개 <span style="color: #025523; font-weight: 600;">쾌적</span>
            </p>
            <hr style="border-top: 1px solid black;">
            <v-row class="col-12" v-if="dong_origin.elementary_count + dong_origin.middle_count + dong_origin.high_count <= 10" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              교육지수 <span style="color: #ff3a29; font-weight: 600; margin-left: 5px;"> 낮음</span>
            </v-row>
            <v-row class="col-12" v-else-if="dong_origin.elementary_count + dong_origin.middle_count + dong_origin.high_count <= 20" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              교육지수 <span style="color: #ff6a07; font-weight: 600; margin-left: 5px;"> 보통</span>
            </v-row>
            <v-row class="col-12" v-else-if="21 <= dong_origin.elementary_count + dong_origin.middle_count + dong_origin.high_count" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              교육지수 <span style="color: #025523; font-weight: 600; margin-left: 5px;"> 높음</span>
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>초등학교 : {{ dong_origin.elementary_count }} 개</v-col>
              <v-col>중학교 : {{ dong_origin.middle_count }} 개</v-col>
              <v-col>고등학교 : {{ dong_origin.high_count }} 개</v-col>
            </v-row>
            <hr style="border-top: 1px solid black;">
            <v-row class="col-12" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              유가정보
            </v-row>
            <v-row class="col-12" style="padding: 0;">
              <v-col>고급 휘발유 : {{ dong_origin.high_oil }} 원</v-col>
              <v-col>휘발유 : {{ dong_origin.oil }} 원</v-col>
              <v-col>경유 : {{ dong_origin.oil2 }} 원</v-col>
            </v-row>
            <hr style="border-top: 1px solid black;">
            <v-row class="col-12" style="font-size: 20px; font-weight: 500; margin-top: 0;">
              안전지수
            </v-row>
            <v-row style="margin-top: -0.9vw;">
              <v-col>발생건수 : {{ dong_origin.total }} 건</v-col>
              <v-col>검거건수 : {{ dong_origin.catch }} 건</v-col>
              <v-col>검거율 : {{ dong_origin.percent }} %</v-col>
            </v-row>
          </div>
        </v-col>
      </v-col>
    </v-row>

  </v-content>
</template>
<script>
    import seoul_coor from '../../assets/seoul';
    import {mapActions} from 'vuex';

    export default {
        data: () => ({
            isImgTrue: false,
            selected_dong: '',
            dong2_name: '',
            dong_origin_name: '',
            dong_origin_recommended: [],
            dong2_recommended: [],
        }),

        methods: {
            ...mapActions("data", ["getListOfDong", "getDong2"]),
            async onSubmit(name) {
                const params = {
                    gu: name,
                };
                await this.getListOfDong(params);
            },
            // 검색 버튼 눌렀을 때
            async getScore() {
                const params = {
                    dong2: '서울특별시' + ' ' + this.dong2_name + ' ' + this.selected_dong,
                };
                await this.getDong2(params);
                this.dong_origin_recommended = [];
                this.dong_origin_recommended.push([this.$store.state.data.dong2.first, this.$store.state.data.dong2.first_mapx, this.$store.state.data.dong2.first_mapy]);
                this.dong_origin_recommended.push([this.$store.state.data.dong2.second, this.$store.state.data.dong2.second_mapx, this.$store.state.data.dong2.second_mapy]);
                this.dong_origin_recommended.push([this.$store.state.data.dong2.third, this.$store.state.data.dong2.third_mapx, this.$store.state.data.dong2.third_mapy]);
                this.loadKakaoMap();
            },
            async initScore() {
                console.log("initScore");
                const params = {dong2: {address: ""}};

                console.log("search2 : " + this.$store.state.data.dong2.address);
                this.$store.commit("data/initDong2", params.dong2);
            },
            loadKakaoMap() {

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
                var positions = [];

                this.dong_origin_recommended.forEach(val => {
                    positions.push({
                        title: val[0],
                        latlng: new kakao.maps.LatLng(val[1], val[2])
                    })
                })

                console.log(positions)

                var imageSrc = "http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

                for (var i = 0; i < positions.length; i++) {

                    // 마커 이미지의 이미지 크기 입니다
                    var imageSize = new kakao.maps.Size(24, 35);

                    // 마커 이미지를 생성합니다
                    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

                    // 마커를 생성합니다
                    var marker = new kakao.maps.Marker({
                        map: map, // 마커를 표시할 지도
                        position: positions[i].latlng, // 마커를 표시할 위치
                        title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
                        image: markerImage // 마커 이미지
                    });
                }

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

                this.dong_origin_recommended.push([this.$store.state.data.dong_info.first, this.$store.state.data.dong_info.first_mapx, this.$store.state.data.dong_info.first_mapy]);
                this.dong_origin_recommended.push([this.$store.state.data.dong_info.second, this.$store.state.data.dong_info.second_mapx, this.$store.state.data.dong_info.second_mapy]);
                this.dong_origin_recommended.push([this.$store.state.data.dong_info.third, this.$store.state.data.dong_info.third_mapx, this.$store.state.data.dong_info.third_mapy]);
                return this.$store.state.data.dong_info
            }
        },
        mounted: function () {
            this.loadKakaoMap();
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

   @media screen and (max-width: 767px) {
      .main-description1{
      font-family: 'Noto Sans KR', sans-serif;
      font-weight: 700;
      font-size: 13px;
      margin-top: -15px;
      margin-left: 1vw;
    }
  }

  .main-description2 {
    color: #6567A8;
    margin-left: 0.8vw;
    margin-right: 0.8vw;
  }

  @media screen and (max-width: 767px) {
    .v-label {
    font-size: 12px !important;
    }
  }

  #map {
    width:550px;
    height:565px;
  }

  @media screen and (max-width: 767px) {
    #map {
      width:500px;
      height:250px;
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

  .map-description {
    font-size: 16px;
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: -40px;
  }

  @media screen and (max-width: 767px) {
    .map-description {
      font-size: 14px;
      font-family: 'Noto Sans KR', sans-serif;
  }
  }
</style>