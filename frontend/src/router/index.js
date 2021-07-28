import { createWebHistory, createRouter } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('@/views/HomeView.vue'),
    },
    {
        path: '/rasq/',
        name: 'RandomSequenceGenerator',
        component: () => import('@/views/RandomSequenceView.vue'),
    },
    {
        path: '/memo/',
        name: 'Memo',
        component: () => import('@/views/MemoView.vue')
    },
    {
        path: '/:catchAll(.*)',
        name: 'Page not found',
        component: () => import('@/views/PageNotFoundView.vue'),
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
