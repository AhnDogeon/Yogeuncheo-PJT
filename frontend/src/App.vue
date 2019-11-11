<template>
    <v-app id="app">
        <v-container class="container-box">
            <v-layout class="layout-box" justify-center style="margin-top: 5vh;">
                <p style="margin-left: 8vw;" @click="goMain">
                    요 근 처
                </p>
                <img src="./assets/yo1.png" alt="yo1" class="yo-img1">
                <img src="./assets/yo2.png" alt="yo2" class="yo-img2">
            </v-layout>
            <router-view/>
        </v-container>

        <!-- each pages will be placed here -->

    </v-app>
</template>

<script>
    import router from './router';

    export default {
        components: {
        },
        data: () => ({
            drawer: null,
        }),
        computed: {

        },
        mounted() {

        },
        methods: {

            goMain() {
                this.$router.push('/');
            },

        }
    };
</script>

<style>
    #app {
        background-color: #f2c766;
        font-family: 'Noto Sans KR', sans-serif;
    }

    .layout-box {
        font-family: 'Black Han Sans', sans-serif;
        font-size: 5vw;
    }
    @media screen and (max-width: 767px) {
        .layout-box
        { font-size:50px;
        }
    }


    .yo-img1 {
        height: 5vw;
        position: relative;
        top: 0.5vw;
        -webkit-animation: yo-img1 1s infinite;
        -moz-animation: yo-img1 1s infinite;
        animation: yo-img1 1s infinite;
    }

    @media screen and (max-width: 767px) {
        .yo-img1
        {
        height: 50px;
        position: relative;
        top: 0.5vw;
        -webkit-animation: yo-img1 1s infinite;
        -moz-animation: yo-img1 1s infinite;
        animation: yo-img1 1s infinite;
        }
    }



    @-webkit-keyframes yo-img1 {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @-moz-keyframes yo-img1 {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes yo-img1 {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    .yo-img2 {
        height: 5vw;
        position: relative;
        right: 5.3vw;
        top: 0.6vw;
        -webkit-animation: yo-img2 1s infinite;
        -moz-animation: yo-img2 1s infinite;
        animation: yo-img2 1s infinite;
    }

    @media screen and (max-width: 767px) {
        .yo-img2
        {
        height: 49px;
        position: relative;
        right: 52px;
        -webkit-animation: yo-img2 1s infinite;
        -moz-animation: yo-img2 1s infinite;
        animation: yo-img2 1s infinite;
        }
    }

    @-webkit-keyframes yo-img2 {
        0% {
            opacity: 1;
        }
        100% {
            opacity: 0;
        }
    }

    @-moz-keyframes yo-img2 {
        0% {
            opacity: 1;
        }
        100% {
            opacity: 0;
        }
    }

    @keyframes yo-img2 {
        0% {
            opacity: 1;
        }
        100% {
            opacity: 0;
        }
    }
</style>