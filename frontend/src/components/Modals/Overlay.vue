<template>
    <div id="overlay" @click="handleOnClick()">
        <div id="surface-container">
            <slot name="sSurface"></slot>
        </div>
    </div>
</template>

<script setup>
const emits = defineEmits([
    'onClick'
]);

function handleOnClick() {
    emits('onClick', false);
};
</script>

<style scoped>
#overlay {
    background-color: rgba(219, 219, 222, 0.458);
    backdrop-filter: blur(2px);
    width: 100%;
    height: 100dvh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 50;
}
</style>