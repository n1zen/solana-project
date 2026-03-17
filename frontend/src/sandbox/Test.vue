<template>
    <div id="test">
        <!-- Place component here to view alone -->
        <Nav />
        <!-- <NavButton /> -->
    </div>
</template>

<script setup>
import Nav from '@/components/Nav/Nav.vue';
import NavButton from '@/components/Buttons/NavButton/NavButton.vue';
</script>

<style scoped>
#test {
    background-color: var(--color-primary);
    padding-top: var(--margin-top-main);
    width: 100dvw;
    min-height: 100dvh;
    
    display: flex;
}
</style>