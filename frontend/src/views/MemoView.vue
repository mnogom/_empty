<template>
  <div id="notes-view">
    <span>Memo</span>
    <ul v-for="section in sections"
          v-bind:key="section.id">{{ section.name }}
      <li v-for="note in section.notes"
          v-bind:key="note.id">
        <span>
          name:
          <input type="text"
                 v-bind:id="`note-name-${note.id}`"
                 v-bind:value="note.name">
        </span>
        <span>
          url:
          <input type="text"
                 v-bind:id="`note-url-${note.id}`"
                 v-bind:value="note.url">
        </span>
        <span>
          description:
          <input type="text"
                 v-bind:id="`note-description-${note.id}`"
                 v-bind:value="note.description">
        </span>
        <button v-on:click="update_note(section.id, note.id)">update</button>
        <button v-on:click="delete_note(section.id, note.id)">delete</button>
      </li>
      <li>
        name: <input type="text" v-bind:id="`new-note-name-${section.id}`"><br>
        url: <input type="text" v-bind:id="`new-note-url-${section.id}`"><br>
        description: <input type="text" v-bind:id="`new-note-description-${section.id}`"><br>
        <button v-on:click="create_note(section.id)">add</button>
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
    this.get_memo_sections()
  },


  methods: {
    update_note: function(section_id, note_id) {
      let name = document.getElementById(`note-name-${note_id}`).value
      let url = document.getElementById(`note-url-${note_id}`).value
      let description = document.getElementById(`note-description-${note_id}`).value

      axios({
        method: "PATCH",
        url: `api/memo/sections/${section_id}/notes/${note_id}/`,
        data: {
          name: name,
          url: url,
          description: description,
          section_id: section_id,
        },
      }).then(response => {
        console.log(response.data.detail)
      })
    },

    delete_note: function(section_id, note_id) {
      axios({
        method: "DELETE",
        url: `api/memo/sections/${section_id}/notes/${note_id}/`
      }).then(response => {
        console.log(response.data.detail)
      }).catch(error => {
        console.log(error)
      })
    },

    create_note: function(section_id) {
      let name = document.getElementById(`new-note-name-${section_id}`).value
      let url = document.getElementById(`new-note-url-${section_id}`).value
      let description = document.getElementById(`new-note-description-${section_id}`).value

      axios({
        method: "POST",
        url: `api/memo/sections/${section_id}/notes/`,
        data: {
          name: name,
          url: url,
          description: description,
        }
      }).then(response => {
        console.log(response.data.detail)
      })
    },

    get_memo_sections: function() {
      axios({
        method: "GET",
        url: "api/memo/sections/"
      }).then(response => {
        this.sections = response.data.detail
      })
    }
  }
}
</script>

<style scoped>
ul {
  font-size: large;
}

li {
  font-size: small;
  list-style-type: none;
  border-left: 5px solid rgb(100, 140, 180);
  background-color: rgba(100, 140, 180, 0.1);
  margin: 10px 0px;
  width: 50%;
}

input {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: rgba(255, 255, 255, 0.1);

  font-size: small;
  border: none;
  width: 100%;
  }

input:focus { outline: none; }

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
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