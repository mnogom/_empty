<template>
  <div id="ra-sq-app">
    <NavigationModule/>
    <RandomSequenceModule msg="Generate random sequence"/>
    <FooterModule/>
  </div>
</template>

<script>
import NavigationModule from './components/NavigationModule.vue'
import RandomSequenceModule from './components/RandomSequenceModule.vue'
import FooterModule from "./components/FooterModule.vue"

export default {
  name: 'RaSqApp',
  components: {
    NavigationModule,
    RandomSequenceModule,
    FooterModule,
  }
}
</script>

<style scoped>
  #ra-sq-app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
