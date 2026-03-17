import { createRouter, createWebHistory } from 'vue-router';
import DashboardView from '../views/DashboardView.vue';
import LifecycleView from '../views/LifecycleView.vue';
import AnalyticsView from '@/views/AnalyticsView.vue';
import ProjectsView from '@/views/ProjectsView.vue';
import TeamsView from '@/views/TeamsView.vue';
import InventoryView from '@/views/InventoryView.vue';
import ProductsView from '@/views/ProductsView.vue';
import Test from '@/sandbox/Test.vue';

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/dash',
      redirect: { name: 'dashboard' }
    },
    {
      path: '/home',
      redirect: { name: 'dashboard' }
    },
    {
      path: '/homepage',
      redirect: { name: 'dashboard' }
    },
    {
      path: '/lifecycle',
      name: 'lifecycle',
      component: LifecycleView
    },
    {
      path: '/analytics',
      name: 'analytics',
      component: AnalyticsView
    },
    {
      path: '/projects',
      name: 'projects',
      component: ProjectsView
    },
    {
      path: '/teams',
      name: 'teams',
      component: TeamsView
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: InventoryView
    },
    {
      path: '/products',
      name: 'products',
      component: ProductsView
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    }
  ]
});

export default router;
