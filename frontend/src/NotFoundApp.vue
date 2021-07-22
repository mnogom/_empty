<template>
  <div id="not-found-app">
    <NavigationModule/>
    <span>404 | Page not found</span>
    <FooterModule/>
  </div>
</template>

<script>
import NavigationModule from './components/NavigationModule.vue'
import FooterModule from './components/FooterModule'

export default {
  name: "NotFoundApp",
  components: {
    NavigationModule,
    FooterModule,
  }

}
</script>

<style scoped>
  #not-found-app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  span {
    font-size: larger;
  }
</style>
