<template>
  <div class="container">
    <Nav />
    <main>
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'

import Nav from './components/Nav/Nav.vue';
</script>

<style scoped>
.container {
  background-color: var(--color-primary);
  padding: var(--margin-top-main) 25px 0;
  width: 100%;
  display: flex;
  gap: 50px;
}

main {
  flex: 1;
  min-width: 0;

  width: 100%;
  padding-top: 90px;
  display: flex;
}
</style>