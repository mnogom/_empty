<template>
  <div id="home-app">
    <NavigationComponent/>
    <router-view/>
    <FooterComponent/>
  </div>
</template>

<script>
import NavigationComponent from "./components/NavigationComponent.vue"
import FooterComponent from "./components/FooterComponent.vue"

export default {
  name: "App.vue",
  components: {
    NavigationComponent,
    FooterComponent,
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
  }
</style>
