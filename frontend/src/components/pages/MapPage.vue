<template>
    <v-content>
        <v-layout class="seoul-maps mt-1">
            <!--<img class="seoul-map1" src="../../assets/서울지도1.png" alt="서울지도1">-->
            <!--<img class="seoul-map2" src="../../assets/서울지도2.png" alt="서울지도2" @click="onClickMap">-->
            <div id="map" style="width:500px;height:400px;"></div>
            <button @click="setDraggable(false)">지도 드래그 이동 끄기</button>
            <button @click="setDraggable(true)">지도 드래그 이동 켜기</button>
        </v-layout>
        <v-layout style="margin-left: 45vw;">
            <img v-if="isImgTrue" src="../../assets/역삼동영수증.png" style="width: 25vw;">
        </v-layout>

        <div class="waves1"></div>
        <div class="waves2"></div>
        <div class="waves3"></div>

    </v-content>

</template>

<script>
    export default {

        data: () => ({
            isImgTrue: false,

        }),

        methods: {
            onClickMap() {
                this.isImgTrue = !this.isImgTrue;
            },

        },
        mounted() {
            var container = document.getElementById('map');
            var options = {
                center: new kakao.maps.LatLng(33.450701, 126.570667),
                level: 10
            };
            var map = new kakao.maps.Map(container, options);
            function setDraggable(draggable) {
                console.log('222222222222222');
                map.setDraggable(draggable);
            // 마우스 드래그로 지도 이동 가능여부를 설정합니다
            };
        },
    }
</script>

<style>

    .seoul-maps img {
        width: 40vw;
        position: absolute;
    }

    .seoul-maps > .seoul-map2 {
        opacity: 0;
    }

    .seoul-maps:hover > .seoul-map2 {
        opacity: 1;
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
</style>