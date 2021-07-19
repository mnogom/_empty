<template>
  <div>
    <Navigation/>
    <RandomSequence msg="Generate random sequence"/>
    <div class="framework-info">
      <span>Created  with</span>
      <img alt="Vue logo" src="./assets/logo.png" height="50">
    </div>
  </div>
</template>

<script>
import RandomSequence from './components/RandomSequence.vue'
import Navigation from './components/Navigation.vue'

export default {
  name: 'App',
  components: {
    RandomSequence,
    Navigation,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.framework-info {
  position: absolute;
  bottom: 3rem;
  right: 3rem;
}

</style>
