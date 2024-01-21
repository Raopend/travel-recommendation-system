import {createRouter, createWebHistory} from 'vue-router'


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/login',
            name: 'login',
            component: () => import('@/views/LoginView.vue')
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('@/views/RegisterView.vue')
        },
        {
            path: '/',
            name: 'index',
            redirect: '/home',
            component: () => import('@/views/IndexView.vue'),
            children: [
                {
                    path: 'home',
                    name: 'home',
                    component: () => import('@/views/HomeView.vue')
                },
                {
                    path: 'dashboard',
                    name:'dashboard',
                    component:()=>import('@/views/DashboardView.vue'),
                },
                {
                    path: 'recommend',
                    name:'recommend',
                    component:()=>import('@/views/RecommendView.vue'),
                }
            ]
        }
    ]
})

export default router