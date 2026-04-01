<template>
  <div class="container" v-if="!isTest">
    <Nav />
    <main>
      <RouterView />
    </main>
  </div>
  <div class="test-container" v-else>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView, useRoute } from 'vue-router'
import { ref, watch } from 'vue';

import Nav from './components/Nav/Nav.vue';

const route = useRoute();
const isTest = ref(false);

watch(() => route.path, (newPath, oldPath) => {
  // console.log('Changement de page :', oldPath, '→', newPath);
  isTest.value = newPath === '/test';
});
</script>

<style scoped>
.container {
  background-color: var(--color-primary);
  padding: var(--margin-top-main) 25px 0;
  width: 100%;
  display: flex;
  gap: 50px;
}

.test-container {
  background-color: var(--color-primary);
  height: 100dvh;
  width: 100%;
}

main {
  flex: 1;
  min-width: 0;

  width: 100%;
  padding-top: 90px;
  display: flex;
}
</style>