import { createApp } from "vue"
import axios from "axios"
import router from "./router"

import App from "./App.vue"

// Setup dev and prod base urls for axios
let dev_mode = process.env.NODE_ENV === "development"
axios.defaults.baseURL = dev_mode ? "http://127.0.0.1:8000" : "/"

// Setup url routing
createApp(App).use(router).mount("#app")
