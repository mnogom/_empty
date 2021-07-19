import { createApp, h } from 'vue'
// import App from './App.vue'
import axios from "axios"

// Setup dev and prod base urls for axios
let dev_mode = process.env.NODE_ENV === 'development'
axios.defaults.baseURL = dev_mode ? 'http://127.0.0.1:8000' : '/'

// createApp(App).mount('#app')

// Setup url routing
import App from './App.vue'
import Navigation from './components/Navigation.vue'

// const NotFoundComponent = { template: '<p>Page not found</p>' }

const routes = {
    "/": Navigation,
    "/gers": App,
}

const SimpleRouter = {
    data: () => ({
        currentRoute: window.location.pathname
    }),

    computed: {
        CurrentComponent() {
            return routes[this.currentRoute]
        }
    },

    render() {
        return h(this.CurrentComponent)
    }
}

createApp(SimpleRouter).mount('#app')
