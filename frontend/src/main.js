import { createApp, h } from 'vue'
import axios from "axios"

// Setup dev and prod base urls for axios
let dev_mode = process.env.NODE_ENV === 'development'
axios.defaults.baseURL = dev_mode ? 'http://127.0.0.1:8000' : '/'

// Setup url routing
import RaSqApp from "./RaSqApp.vue"
import HomeApp from "./HomeApp.vue"
import NotFoundApp from "./NotFoundApp.vue"

const routes = {
    "/": HomeApp,
    "/rasq/": RaSqApp,
}

const SimpleRouter = {
    data: () => ({
        currentRoute: window.location.pathname
    }),

    computed: {
        CurrentComponent() {
            return routes[this.currentRoute] || NotFoundApp
        }
    },

    render() {
        return h(this.CurrentComponent)
    }
}

createApp(SimpleRouter).mount('#app')
