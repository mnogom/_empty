<template>
  <div id="random-sequence-component">
    <div>
      {{ msg }} with
      <input v-on:input="edit_count_of_elements($event)"
             value="10"
             type="number"/>
      numbers
    </div>
    <li v-for="(value, key) in elements"
        v-bind:key="key">
      {{ value }}
    </li>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "RandomSequenceComponent",

  props: {
    msg: String
  },

  data: () => ({
    elements_count: 10,
    elements: [],
  }),

  mounted() {
    this.get_random_sequence()
  },

  methods: {
    edit_count_of_elements: function (event) {
      let event_value = Number(event.target.value)

      if (event_value > 10) {
        event.target.value = 10
        event_value = 10
      } else if (event_value < 0) {
        event.target.value = 0
        event_value = 0
      }

      if (event_value !== this.elements_count) {
        this.elements_count = event_value
        this.get_random_sequence()
      }
    },

    get_random_sequence: function () {
      axios({
            method: "get",
            url: "api/random/sequence/",
            params: {
              count: this.elements_count
            }
          }).then(response => {
            this.elements = response.data
          })
    }
  }
}
</script>

<style scoped>

  input {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;

    font-size: medium;
    border: none;
    width: 2em;
  }

  input:focus { outline: none; }

  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
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
