<template>
  <div id="navigation-component">
    <router-link to="/">home</router-link>
    <router-link to="/rasq/">rasq</router-link>
    <router-link to="/new/not/developed/feature">nefe</router-link>
  </div>
</template>

<script>
export default { name: "NavigationComponent", }
</script>

<style scoped>
  #navigation-component { margin: 1rem 0; }
  a { padding: 0 1rem; }
</style>
