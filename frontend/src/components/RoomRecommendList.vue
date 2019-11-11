<template>
    <v-content class="room-recommend">
        <v-layout class="mt-10 layout-box1 mx-auto">
        </v-layout>
        <v-layout justify-center>
            <p class="recommend-title">
                요즘 뜨는 동네
            </p>
        </v-layout>
        <v-layout justify-center>
            <div>
                <v-sheet
                        class="mx-auto"
                        max-width="76vw"
                        style="background-color: #F2C766;"
                >
                    <v-slide-group
                            v-model="model"

                            :show-arrows="showArrows"
                    >
                        <v-slide-item
                                v-for="(item, n) in items"
                                :key="n"
                                v-slot:default="{ active, toggle }"
                        >
                          <a target="_blank"
                             :href="item.url">
                            <v-card flat
                                    color="#00ff0000"
                                    class="card1"
                                    @click="onCardClick(n)"
                            >
                                <v-img :src="item.src" height="7.8vw">
                                </v-img>

                                    <v-card-text class="card-description">

                                        <v-layout class="description-title">
                                            {{ item.description1 }}
                                        </v-layout>
                                        {{ item.description2 }}

                                    </v-card-text>

                            </v-card>
                          </a>
                        </v-slide-item>
                    </v-slide-group>
                </v-sheet>
            </div>
        </v-layout>
    </v-content>
</template>

<script>
    export default {
        data: () => ({
            model: null,
            showArrows: true,
            items: [
                {
                    src: require('../assets/동교동.jpg'),
                    description1: '동교동',
                    description2: '핫플레이스',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%8F%99%EA%B5%90%EB%8F%99+%ED%95%AB%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4'
                },
                {
                    src: require('../assets/망원동.jpg'),
                    description1: '망원동',
                    description2: '분위기 좋은 카페',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%A7%9D%EC%9B%90%EB%8F%99+%EB%B6%84%EC%9C%84%EA%B8%B0+%EC%A2%8B%EC%9D%80+%EC%B9%B4%ED%8E%98'
                },
                {
                    src: require('../assets/성수동.png'),
                    description1: '성수동',
                    description2: '블루보틀',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%B1%EC%88%98%EB%8F%99+%EB%B8%94%EB%A3%A8%EB%B3%B4%ED%8B%80'
                },
                {
                    src: require('../assets/신사동.jpg'),
                    description1: '신사동',
                    description2: '가로수길',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%8B%A0%EC%82%AC%EB%8F%99+%EA%B0%80%EB%A1%9C%EC%88%98%EA%B8%B8'
                },
                {
                    src: require('../assets/신사동1.jpg'),
                    description1: '신사동',
                    description2: '인싸들만 가는 카페',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%8B%A0%EC%82%AC%EB%8F%99+%EC%9D%B8%EC%8B%B8%EB%93%A4%EB%A7%8C+%EA%B0%80%EB%8A%94+%EC%B9%B4%ED%8E%98'
                },
                {
                    src: require('../assets/역삼동.jpg'),
                    description1: '역삼동',
                    description2: '트리하우스',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%97%AD%EC%82%BC%EB%8F%99+%ED%8A%B8%EB%A6%AC%ED%95%98%EC%9A%B0%EC%8A%A4',

                },
                {
                    src: require('../assets/연남동.png'),
                    description1: '연남동',
                    description2: '연트럴파크',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%97%B0%EB%82%A8%EB%8F%99+%EC%97%B0%ED%8A%B8%EB%9F%B4%ED%8C%8C%ED%81%AC'
                },
                {
                    src: require('../assets/을지로.jpg'),
                    description1: '을지로',
                    description2: '힙한 카페',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%9D%84%EC%A7%80%EB%A1%9C+%ED%9E%99%ED%95%9C+%EC%B9%B4%ED%8E%98'
                },
                {
                    src: require('../assets/이태원.jpg'),
                    description1: '이태원',
                    description2: '야경이 좋은 곳',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%9D%B4%ED%83%9C%EC%9B%90+%EC%95%BC%EA%B2%BD%EC%9D%B4+%EC%A2%8B%EC%9D%80+%EA%B3%B3'
                },
                {
                    src: require('../assets/익선동.jpg'),
                    description1: '익선동',
                    description2: '고즈넉한 한옥마을',
                    url: 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%9D%B5%EC%84%A0%EB%8F%99+%EA%B3%A0%EC%A6%88%EB%84%89%ED%95%9C+%ED%95%9C%EC%98%A5%EB%A7%88%EC%9D%84'
                },
            ]
        }),
        methods: {
            onCardClick(n) {
                this.n = n - 1;
            }
        }
    };
</script>

<style>
    .room-recommend {
        margin: auto;
    }

    .layout-box1 {
        border-bottom: 0.1vh solid #605b5b;
        width: 70vw;
    }

    .recommend-title {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 2vw;
        font-weight: 500;
        margin-top: 3vh;
        margin-bottom: 5vh;
    }

    @media screen and (max-width: 767px) {
        .recommend-title
        {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 18px;
        font-weight: 500;
        margin-top: 3vh;
        margin-bottom: 5vh;
        }
    }

    .v-slide-group {
        background-color: #F2C766;
    }

    .card1 {
        margin: 0 1vw;
        width: 144px;
    }

    @media screen and (max-width: 767px) {
        .card1 {
            margin: 0 1vw;
            width: 100px;
        }
    }


    .card-description {
        background: rgba(255, 255, 255, 0.8);
        font-weight: 500;
        font-family: 'Noto Sans KR', sans-serif;
        padding: 1.1vh 1vw;
        font-size: 14px;
    }

    @media screen and (max-width: 767px) {
        .card-description {
            background: rgba(255, 255, 255, 0.8);
            font-weight: 500;
            font-family: 'Noto Sans KR', sans-serif;
            padding: 1.1vh 1vw;
            font-size: 12px;
    }
    }

    .description-title {
        font-weight: 900;
        font-family: 'Noto Sans KR', sans-serif;
        margin-bottom: 0.2vh;
    }

    .v-slide-group__next, .v-slide-group__prev {
        margin: auto !important;
    }


</style>