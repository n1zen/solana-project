<template>
    <div class="simple-progress-bar">
        <div 
            class="progress" 
            :style="{ 
                backgroundColor: 
                inputsValue[index] === '' ||
                inputsValue[index] === undefined ? 
                defaultColor : doneColor 
            }"
            v-for="(item, index) in inputsValue" 
            :key="index" 
            :id="'progress-bar-'+index"
        ></div>
    </div>
</template>

<script setup>
const props = defineProps({
    inputsValue: {
        type: Array,
        default: []
    },
    defaultColor: {
        type: String,
        default: "#000"
    },
    doneColor: {
        type: String,
        default: 'green'
    },
});
</script>

<style scoped>
.simple-progress-bar {
    display: flex;
    align-items: center;
    gap: 3px;
}

.progress {
    flex-grow: 1;
    
    border-radius: 3px;
    height: 5px;
    transition: 0.3s;
}
</style>