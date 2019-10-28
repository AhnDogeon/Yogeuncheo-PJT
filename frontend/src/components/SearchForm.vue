<template>
  <v-form ref="form">
    <v-layout justify-center class="main-description1">
      이사할 곳이
      <span class="main-description2">
        어떤 동네
      </span>
      인지 궁금한가요?
    </v-layout>

    <v-layout class="search-form">
      <v-text-field v-model="title" label="OO구 OO동을 검색해보세요" outlined/>
      <v-btn text icon class="ml-1" @click.stop="dialogOpen = true">
        <v-icon large>mdi-magnify</v-icon>
      </v-btn>
    </v-layout>
    <ModalForm v-on:dialogClose="dialogClose" :dialogOpen="dialogOpen"></ModalForm>
  </v-form>
</template>

<script>
    import ModalForm from '@/components/ModalForm'

    export default {
        props: {
            submit: {
                type: Function,
                default: () => {
                }
            }
        },
        components: {
            ModalForm,
        },
        data: () => ({
            title: "",
            dialogOpen: false,

        }),
        methods: {
            onSubmit: function () {
                const params = {
                    title: this.title,
                };
                this.submit(params);
            },
            dialogClose() {
                this.dialogOpen = false
            }
        },
    };
</script>

<style>
  .main-description1 {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 700;
    font-size: 2vw;
    margin-top: 2vh;
  }

  .main-description2 {
    color: #6567A8;
    margin-left: 0.7vw;
  }

  .search-form {
    width: 30vw;
    margin: 8vh auto 0;
  }
</style>