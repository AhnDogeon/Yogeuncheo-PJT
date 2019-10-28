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
          max-width="1200"
        >
          <v-slide-group
            v-model="model"
            class="pa-4"
            :prev-icon="prevIcon ? 'mdi-minus' : undefined"
            :next-icon="nextIcon ? 'mdi-plus' : undefined"
            :show-arrows="showArrows"
          >
            <v-slide-item
              v-for="(item, n) in items"
              :key="n"
              v-slot:default="{ active, toggle }"
            >
              <v-card
                :color="active ? 'primary' : 'grey lighten-1'"
                class="ma-4"
                height="180"
                width="145"
                @click="onCardClick(n)"
                :img="item.src"
              >
                <v-card-text class="card-description py-2">
                  <v-layout class="description-title">
                    {{ item.description1 }}
                  </v-layout>
                  {{ item.description2 }}
                </v-card-text>
              </v-card>
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
      },
      {
        src: require('../assets/망원동.jpg'),
        description1: '망원동',
        description2: '분위기 좋은 카페',
      },
      {
        src: require('../assets/성수동.png'),
        description1: '성수동',
        description2: '블루보틀',
      },
      {
        src: require('../assets/신사동.jpg'),
        description1: '신사동',
        description2: '가로수길',
      },
      {
        src: require('../assets/신사동1.jpg'),
        description1: '신사동',
        description2: '인싸들만 가는 카페',
      },
      {
        src: require('../assets/역삼동.jpg'),
        description1: '역삼동',
        description2: '트리하우스',

      },
      {
        src: require('../assets/연남동.png'),
        description1: '연남동',
        description2: '연트럴파크',
      },
      {
        src: require('../assets/을지로.jpg'),
        description1: '을지로',
        description2: '힙한 카페',
      },
      {
        src: require('../assets/이태원.jpg'),
        description1: '이태원',
        description2: '야경이 좋은 곳',
      },
      {
        src: require('../assets/익선동.jpg'),
        description1: '익선동',
        description2: '고즈넉한 한옥마을',
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

  .pa-4 {
    background-color: #F2C766;
  }

  .card-description {
    background: rgba(255, 255, 255, 0.8);
    margin-top: 16.8vh;
    font-weight: 500;
    font-family: 'Noto Sans KR', sans-serif;
  }

  .description-title {
    font-weight: 900;
    font-family: 'Noto Sans KR', sans-serif;
  }

</style>