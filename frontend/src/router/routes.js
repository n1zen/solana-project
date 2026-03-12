import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '../views/DashboardView.vue';
import Test from '@/sandbox/Test.vue';

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    }
  ]
});

export default router;
