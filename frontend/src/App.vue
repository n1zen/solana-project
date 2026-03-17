<template>
    <Nav />
    <main> 
      <RouterView />
    </main>
</template>

<script setup>
import { RouterView } from 'vue-router'

import Nav from './components/Nav/Nav.vue';
</script>

<style>
#app {
    background-color: var(--color-primary);
    padding-top: var(--margin-top-main);
    width: 100dvw;
    min-height: 100dvh;
    display: flex;
    gap: 50px
}

main {
  width: 100%
}
</style>