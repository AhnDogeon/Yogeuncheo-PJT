<template>
  <v-content class="content-box">

      <SearchForm></SearchForm>
      <RoomRecommendList></RoomRecommendList>

  </v-content>
</template>

<script>
  import SearchForm from "../SearchForm";
  import RoomRecommendList from "../RoomRecommendList";
  export default {
      components: {
          SearchForm,
          RoomRecommendList
      },
  }
</script>

<style>

</style>