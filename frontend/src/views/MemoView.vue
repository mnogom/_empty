<template>
  <div id="notes-view">
    <span>Memo</span>
    <ul v-for="section in sections"
          v-bind:key="section.id">{{ section.name }}
      <li v-for="note in section.notes"
          v-bind:key="note.id">
        <a v-bind:href="note.url">{{ note.name }}</a>
        <button>edt</button>
        <button>rmv</button>
        <div v-show="note.description"
             class="note-description">{{ note.description }}</div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "NoteView.vue",

  data: () => ({
    sections: [],
  }),

  mounted() {
    axios({
      method: "get",
      url: "api/memo/sections/"
    }).then(response => {
      this.sections = response.data.detail
    })
  }
}
</script>

<style scoped>
ul {
  font-size: large;
  width: 400px;
}

li {
  font-size: small;
  list-style-type: none;
  border-left: 5px solid rgb(100, 140, 180);
  background-color: rgba(100, 140, 180, 0.1);
  margin: 10px 0px;
  width: 400px;
}

button {
  border: none;
  background-color: rgba(0, 0, 0, 0.2)
}

button:hover {
  background-color: red;
}

.note-description { font-style: italic; }
</style>