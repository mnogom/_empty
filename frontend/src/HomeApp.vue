<template>
  <div id="home-app">
    <NavigationModule/>
    <span>Home page</span>
    <FooterModule/>
  </div>
</template>

<script>
import NavigationModule from "./components/NavigationModule.vue";
import FooterModule from "./components/FooterModule.vue"

export default {
  name: "HomeApp.vue",
  components: {
    NavigationModule,
    FooterModule,
  }
}
</script>

<style scoped>
  #home-app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
