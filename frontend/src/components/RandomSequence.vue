<template>
  <div>
    <div class="top">{{ msg }}</div>
    <li v-for="(value, key) in elements" v-bind:key="key">
      {{ value }}
    </li>
  </div>
</template>

<script>

import axios from 'axios'

export default {

  name: 'HelloWorld',

  props: {
    msg: String
  },

  data: () => ({
    elements: []
  }),

  mounted() {
    axios({
      method: 'get',
      url: 'api/random'
    }).then(response => {
      this.elements = response.data
    })

  }

}

</script>

<style scoped>

h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0.5em;
}

li {
  display: inline-block;
  padding: 0.5em;
  margin: 10px 10px;
}

li:hover {
  background-color: #2c3e50;
  color: white;
}

</style>
