<template>
    <div id="footer-component">
      <span>Created  with</span>
      <img alt="Vue logo" src="../assets/logo.png" height="20">
    </div>
</template>

<script>
export default { name: "FooterComponent", }
</script>

<style scoped>
  #footer-component {
    position: absolute;
    bottom: 1rem;
    right: 1rem;
    font-size: small;
  }
</style>
